import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Houses from './config/Houses';
import Core from './core/Core';
import HousesCreate from './config/HousesCreate';
import HousesUpdate from './config/HousesUpdate';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={Core} />
          <Route path='/config/houses' Component={Houses} />
          <Route path='/config/houses/create' Component={HousesCreate} />
          <Route path='/config/houses/:id/update' Component={HousesUpdate} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
