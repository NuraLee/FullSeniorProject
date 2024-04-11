import './Components/Header'
import './App.css';
import { BrowserRouter as Router, Route, Routes, createBrowserRouter, RouterProvider } from 'react-router-dom';
import Header from './Components/Header';
import SearchBar from './Components/SearchBar';
import List from './Components/List'
import Greenlight from './Pages/Greenlight';
import Home from './Pages/Home';
import Account from './Pages/Account';
import Biology from './Pages/Category/Biology';
import Chemistry from './Pages/Category/Chemistry';
import Physics from './Pages/Category/Physics';
import History from './Pages/Category/History';
import Worksheet from './Pages/Worksheet'
import Author from './Pages/Author';
const router = createBrowserRouter([
  {
    path: '/',
    element: <Home/>
  },
  {
    path: '/green-page',
    element: <Greenlight/>
  },
  {
    path: '/Account',
    element: <Account/>
  },
  {
    path: '/category/biology',
    element: <Biology/>
  },
  {
    path: '/category/chemistry',
    element: <Chemistry/>
  },
  {
    path: '/category/physics',
    element: <Physics/>
  },
  {
    path: '/category/history',
    element: <History/>
  },
  {
    path: '/worksheets/:value',
    element: <Worksheet/>
  },
  {
    path: 'authors/:value',
    element: <Author/>
  },

])
function App() {
  return (
    <div>
      <Header/>
    <div className="body">
      
      <RouterProvider router={router}></RouterProvider>
    </div>
    </div>
  );
}

export default App;
