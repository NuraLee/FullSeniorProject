from openai import AsyncOpenAI, OpenAI

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.utils import timezone
from django.db.models import F

from accounts.models import RoomMessage


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def get_gpt_analyze(customer_id: int, message_id: int, message: str, max_tokens: int = 600) -> str:
	"""
    Get GPT analyze for a given message.

    Parameters:
    - message (str): The input message to analyze.
	- engine (str): gpt engine
    - max_tokens (int): The maximum number of tokens in the generated response.

    Returns:
    str: The generated response from GPT.

    Example:
    ```python
    message_to_analyze = "This is the message you want to analyze."
    result = get_gpt_response(message_to_analyze)
    print(result)
    ```
    """

	system_msg = 'You are a helpful assistant'
	prompt = 'Just answer to text below\nText:'

	try:
		chat_completion = client.chat.completions.create(
			messages=[
				{"role": "system", "content": system_msg},
				{"role": "user", "content": f'{prompt}\n{message}'}
			],
			model=settings.OPENAI_MODEL
		)

		response_body = chat_completion.choices[0].message.content

		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			f'chat_{customer_id}',
			{
				'type': 'gpt_answer',
				'message': response_body,
				'message_id': message_id
			}
		)
			
		RoomMessage.objects.filter(pk=message_id).update(response_body=response_body)

	except Exception as ex:
		return 'Сервер перегружен'
