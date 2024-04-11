import '../Components/Header'
import img from './../Assets/kids.png'
import List from '../Components/List';
import { Link } from 'react-router-dom';
function Account() {
  return (
    <div style={{marginTop:"100px", marginLeft:"90px"}}>
      <div style={{display:"flex"}}>
        <div style={{width: '300px', height:'300px', marginRight:'120px', borderRadius:'100%'}}>
          <img src={img} style={{width:'100%'}}></img>
        </div>
        <div style={{marginTop:"10px"}}>
          <h1>Alan Tyreev</h1>
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
          <List/>
        </div>
      </div> 
    
    </div>
  );
}

export default Account;