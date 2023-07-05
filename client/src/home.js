import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {useEffect, useState} from 'react'
import { Link } from 'react-router-dom';


function Home() {

const [data, setData] = useState([])
const [name, setName] = useState("")
const [price, setPrice] = useState("")

useEffect(()=> {
    axios.get('/api')
        .then( (response)=> {setData(response.data)})
        .catch( (error) => {console.log(error)})


        // .then( (response) => response.json())
        // .then( (d)=> setData(d))
}, [])

    function submit () {
        axios.post('/api', {name, price})
            .then( (response) => {console.log(response.data)})
            .catch( (error) => {console.log(error)})
    }

    function delete_product(id) {
        axios.delete('/api/delete/' + id)
            .then( (response) => {console.log(response.data)})
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

    {

        data.map( (d, i) => (
            <div>
            <h4 key={i}>{d.name}, {d.price}</h4>
            
            <form onSubmit={ () => {delete_product(d.id)}}>
                <button>Delete</button>
            </form>
                <Link to={ `update/${d.id}` }>Update</Link>
            </div>
        )
        )
    }

</div>
  );
}

export default Home;
