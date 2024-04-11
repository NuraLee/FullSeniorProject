// PageComponent.js
import { Link } from 'react-router-dom';
import Worksheets from '../Components/Worksheets.json'
import React from 'react';
import { useParams } from 'react-router-dom';
import List from '../Components/List';
import img from './../Assets/img.jpg'
const Author = (props) => {
    const { value } = useParams();
    const data = Worksheets
    const cardStyle = {
      marginBottom: '40px',
      
      display: 'flex', 
      color: 'black',
      width: '700px',
      height: '262px',
      
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
  return (
    <div>
      <div style={{marginTop:"100px", marginLeft:"90px"}}>
      <div style={{display:"flex"}}>
        <div style={{marginRight:'120px', borderRadius:'100%'}}>
          <img src={img} style={{width:'100%'}}></img>
        </div>
        <div style={{marginTop:"10px"}}>
          <h1>{data.at(value - 1).author}</h1>
          <h2 style={{color:"grey"}}>Teacher of Geography</h2>
        </div>
      </div>
      <div style={{marginTop:'100px', display: "flex"}}>
        <div style={{display:'flex', flexDirection:'column', justifyContent:'space-between', border: '0.5px solid #b2bac8', width: '300px', height: '400px', borderRadius:'8px'}}>
          <Link style={{color:"grey", fontSize:"25px", marginTop:"45px"}}>Your recent downloads</Link>
          <Link style={{color:"grey", fontSize:"25px"}}>Your favourite</Link>
          <Link style={{color:"grey", fontSize:"25px"}}>Your suggested content</Link>
          <Link style={{color:"grey", fontSize:"25px", marginBottom:"45px"}}>Change personal information</Link>
        </div>
        <div style={{marginLeft: "100px"}}>
        {data
    .filter(item => item.author === data.at(value - 1).author)
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
    
    </div>
      
    </div>
  );
};

export default Author;
