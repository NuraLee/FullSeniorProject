// GreenlightPage.js

import React from 'react';
import CategoryList from '../Components/CategoryList';
import SearchBar from '../Components/SearchBar';
import ResponsiveAppBar from '../Components/Header';
import { Routes, Route, Router, Link } from 'react-router-dom';

function Greenlight() {
  const categories = ['History', 'Chemistry', 'Biology', 'Physics', 'English', 'Math', 'Literature'];
  const buttonStyle = {
    width: '325px', // Set the width of the button
    height: '325px', // Set the height of the button
    backgroundColor: '#89CFF0', // Set the background color of the button
    color: 'white', // Set the text color
    fontSize: '24px', // Set the font size
    fontWeight: 'bold', // Set the font weight
    textAlign: 'center', // Center align text
    lineHeight: '200px', // Center align vertically
    textDecoration: 'none', // Remove underline
    border: 'none', // Remove border
    cursor: 'pointer', // Set cursor to pointer on hover
    transition: 'background-color 0.3s', // Smooth transition on hover
    marginRight: "30px"
  };
  return (
  
    <div>
      <div style={{marginTop:"50px"}}>
        <SearchBar/>
      </div>
      <div style={{marginTop:'100px'}}>
        <h1>Categories by subject</h1>
        <div className="category-list-container">
      
        <div style={{marginTop:"30px"}} className="category-list">
          {categories.map((category, index) => (
            <div key={index} className="category-item">
              <Link to={`/category/${category}`} className="category-link">
                <button style={buttonStyle} className="category-block">{category}</button>
              </Link>
            </div>
          ))}
        </div>
        </div>
      </div>
    </div>
  );
}

export default Greenlight;
