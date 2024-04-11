import React from 'react';
import { Link } from 'react-router-dom';
import Worksheets from './Worksheets.json';
import img from '../Assets/img.jpg';

const List = () => {
  const cardStyle = {
    marginBottom: '40px',
    display: 'flex',
    color: 'black',
    width: '700px',
    height: '262px',
    border: '0.5px solid #b2bac8',
    borderRadius: '8px',
    padding: '30px 40px',
    boxSizing: 'border-box',
    gap: '40px',
  };

  return (
    <div>
      {Worksheets.map((item) => (
        <div key={item.id} style={cardStyle}>
          <div style={{ width: '350px' }}>
            <img src={img} alt="img" style={{ width: "100%", height: "100%", borderRadius: "3%" }} />
          </div>
          <div>
            <h3><Link to={`/worksheets/${item.id}`}>{item.name}</Link></h3>
            <p>By <Link to={`/authors/${item.id}`}>{item.author}</Link> in <Link to={`/category/${item.subject}`}>{item.subject}</Link>, {item.grade}</p>
            <p>15 Downloads</p>
          </div>
          <div>
            <div><button style={buttonStyle}>Free</button></div>
            <div><Link to={`/worksheets/${item.id}`}><button style={buttonStyle1}> View </button></Link></div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default List;
