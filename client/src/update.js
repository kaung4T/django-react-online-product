import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {useEffect, useState} from 'react'
import { Link, useParams, useNavigate } from 'react-router-dom';


function Update() {

const [data, setData] = useState([])
const [name, setName] = useState("")
const [price, setPrice] = useState("")
const {id} = useParams()
const navigate = useNavigate()



    function submit (e) {
        e.preventDefault()
        axios.put('/api/update/' + id, {name, price})
            .then( (response) => {
                console.log(response.data)
                navigate('/home')
            })
            .catch( (error) => {console.log(error)})
    }

  return (
    <div style={{width: '200px', margin: 'auto', marginTop: '70px'}}>
    <h4>Hello</h4>

    <form onSubmit={submit}>
        <label>Name</label>
        <input type='text' onChange={ (e) => {setName(e.target.value)}} />
        <br></br><br></br>

        <label>Price</label>
        <input type='number' onChange={ (e) => {setPrice(e.target.value)}} />
        <br></br><br></br>
        <button>Submit</button>

    </form>


</div>
  );
}

export default Update;
