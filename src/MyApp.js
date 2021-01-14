import React, {useState, useEffect} from 'react';
import Table from './Table'
import Form from './Form';
import axios from 'axios';

async function fetchAll(){
  try {
     const response = await axios.get('http://localhost:5000/users');
     return response.data.users_list;     
  }
  catch (error){
     //We're not handling errors. Just logging into the console.
     console.log(error); 
     return false;         
  }
}

function MyApp() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetchAll().then( result => {
       if (result)
          setCharacters(result);
     });
  }, [] );
  
  function updateList(person) {
    setCharacters([...characters, person]);
  }

  function removeOneCharacter (index) {
    const updated = characters.filter((character, i) => {
       return i !== index
    });
    setCharacters(updated);
 }

  return (
    <div className="container">
      <Table characterData={characters} removeCharacter={removeOneCharacter} />
      <Form handleSubmit={updateList} />
    </div>
  )
}

export default MyApp;