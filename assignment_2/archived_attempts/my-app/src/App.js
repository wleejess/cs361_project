import logo from './cuteflower.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          Flowers for Friends
        </h1>
        <button onClick={newFlower}>Pick a flower!</button>
      </header>
    </div>
  );
}

function newFlower(){
  console.log("Button clicked ...")
}

export default App;
