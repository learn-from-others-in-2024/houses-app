import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Houses from './config/Houses';
import Core from './core/Core';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={Core} />
          <Route path='/config/houses' Component={Houses} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
