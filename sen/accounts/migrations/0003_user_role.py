# Generated by Django 4.2.7 on 2023-11-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'expert'), (2, 'customer')], default=2),
        ),
    ]
