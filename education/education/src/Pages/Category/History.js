import Worksheets from './../../Components/Worksheets.json'
import { Link } from 'react-router-dom';
import img from '../../Assets/kids.png'
function History() {
    const data = Worksheets
    const cardStyle = {
        marginTop: '30px',
        marginLeft: '35%',
        display: 'flex', 
        
        width: '700px',
        height: '262px',
        margin: '30px',
        border: '0.5px solid #b2bac8', // You can customize the border color
        borderRadius: '8px', // Adjust the border radius as needed
        padding: '30px 40px', // Padding values (top, right, bottom, left)
        boxSizing: 'border-box',
        
        gap: '40px', // Gap between child elements
        
      };
      const buttonStyle = {
        width: '77px',
        height: '44px',
        padding: '8px 16px', // Adjust the padding as needed
        margin: '5px', // Gap between elements
        backgroundColor: '#23A6F0', // Set the background color to your preference
        color: '#fff', // Set the text color to your preference
        border: '1px solid #0073e6', // Customize the border color if desired
        borderRadius: '4px', // Adjust the border radius as needed
        cursor: 'pointer', // Add a pointer cursor for interaction
        marginBottom: '80px',
        marginRight: '-5px'
      };
      const buttonStyle1 = {
        width: '77px',
        height: '44px',
        padding: '8px 16px', // Adjust the padding as needed
        margin: '5px', // Gap between elements
        backgroundColor: '#23A6F0', // Set the background color to your preference
        color: '#fff', // Set the text color to your preference
        border: '1px solid #0073e6', // Customize the border color if desired
        borderRadius: '4px', // Adjust the border radius as needed
        cursor: 'pointer', // Add a pointer cursor for interaction
        marginRight: '-5px',
        marginBottom: '-5px'
      };
    //create a new array by filtering the original array

    return (
      <div>
        <h1>History</h1>
        <p style={{width:"800px"}}>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ut dui consectetur risus commodo finibus. Aliquam id bibendum ante. Aenean convallis in nisl sed cursus. Nulla volutpat placerat sem sed consequat. Donec molestie eleifend tellus eu tristique. Aenean quis blandit tellus, id gravida lorem. Etiam porttitor tincidunt nibh ullamcorper gravida.

Curabitur id dui eu sapien porttitor luctus. Mauris nec tortor blandit, congue tortor vitae, vulputate leo. Vivamus eget tristique urna. Suspendisse convallis est egestas est sollicitudin, vitae aliquet nisl euismod. Nunc et nisl aliquet, posuere dolor ac, condimentum mi. Praesent eget tellus in arcu interdum pretium eget vel nulla. Proin faucibus rutrum volutpat. Etiam pellentesque ultrices nisl, nec gravida dolor malesuada quis.

Vestibulum quis pulvinar dolor. Nullam id luctus tellus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer a dignissim lacus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam semper est ac sem sagittis, sit amet faucibus velit laoreet. Integer in ultricies augue, eu vulputate urna.

Nunc imperdiet tortor ac viverra elementum. In at eros condimentum, porta enim tempor, iaculis leo. Sed eu mi hendrerit, imperdiet neque a, faucibus magna. Quisque viverra, orci vitae semper venenatis, nunc dolor venenatis sapien, vitae lobortis lorem enim sit amet quam. Vivamus ac arcu pharetra, consequat mauris a, aliquam lectus. Integer semper facilisis massa, eu viverra lacus malesuada in. Maecenas a leo et metus convallis efficitur sed nec turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent fringilla est pellentesque, fermentum diam eu, elementum dolor. Fusce quis enim molestie, placerat quam non, pulvinar leo. Etiam nec ipsum nisl. Donec in turpis sed dui luctus vulputate.

Maecenas maximus nisi id massa bibendum, at ultricies quam varius. Curabitur accumsan maximus leo, vel luctus diam hendrerit sed. Sed posuere rutrum ipsum ac pulvinar. Quisque posuere quam elit, dictum finibus magna mollis ut. Phasellus sollicitudin metus quis leo gravida lacinia. Pellentesque ac efficitur nisi. Proin mattis, nibh ut tincidunt varius, nulla nunc faucibus nisi, ac tempor eros nibh eu lacus.</p>
<div style={{marginTop: "50px"}}>
{data
    .filter(item => item.subject === "History")
    .map(item => (
        <div style={cardStyle} >
                    <div><img  src={img} alt="img"/>
                </div>
                <div>
                    <h3 key={item.id}><Link to={`/worksheets/${item.id}`}>{item.name}</Link></h3>
                    <p key={item.id}>By <Link to={`/authors/${item.id}`}>{item.author}</Link> in <Link to={`/category/${item.subject}`}>{item.subject}</Link>, {item.grade}</p>
                    <p>15 Downloads</p>
                </div>
                <div>
                    <div><button style={buttonStyle}>Free</button></div>
                    <div ><Link to={`/worksheets/${item.id}`}><button style={buttonStyle1}> View </button></Link></div>
                </div>
                </div>
    ))
}

        </div>
      </div>
    );
  }
  
  export default History;
  