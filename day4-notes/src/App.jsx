import { useState } from "react";

function App(){

  const [notes,setNotes]=useState([]);
  const [input,setInput]=useState("");

  const addNote =() =>{
    if(input.trim() === "") return;//if user has inputed a empty note
    const newNote ={ id:Date.now(),text:input.trim() };//assigns id with a today date in milliseconds to generate a unique id
    setNotes([... notes,newNote]);
    setInput("");
  };

  const deleteNote=(id) =>{
    setNotes(notes.filter((note)=> note.id !== id))
  };

  return(
    <div>
      <h1>Notes App</h1>
      <p>{notes.length} note{notes.length !== 1 ? "s" : ""}</p>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a Note..."
        />
        <button onClick={addNote}>Add</button>


        <ul>
          {notes.map((note) => 
          (<li key={note.id}>{note.text}
            <button onClick={() => deleteNote(note.id)}>Delete</button>
           </li>
          ))}
        </ul>
    </div>
  );
}

export default App;