import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Houses from './config/Houses';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/config/houses' Component={Houses} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
