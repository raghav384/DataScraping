import logo from './logo.svg';
import './App.css';
function App() {
  return (
    < div className="App">
      <input type="text" placeholder="Enter item to be searched" style={elementStyle} onChange={(e)=>this.searchSpace(e)} />
      {items}
    </div>
  );
}

export default App;
