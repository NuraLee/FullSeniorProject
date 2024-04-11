// PageComponent.js
import img from './../Assets/kids.png'
import Worksheets from '../Components/Worksheets.json'
import React from 'react';
import { useParams } from 'react-router-dom';
const View = (props) => {
    const { value } = useParams();
    const data = Worksheets
  return (
    <div style={{marginTop:"120px", marginLeft:"80px"}}>
      <img src={img}></img>
      <h1>{data.at(value - 1).name}</h1>
      <h2>{data.at(value - 1).author}</h2>
      <h3>{data.at(value - 1).grade}</h3>
    </div>
  );
};

export default View;
