import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {Routes, Route, BrowserRouter} from 'react-router-dom'
import Home from './home';
import Update from './update';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/home' element={<Home />}></Route>
        <Route path='/home/update/:id' element={<Update />}></Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
