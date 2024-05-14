import React from 'react';
import './App.css';
import Nav from './interfaces/Nav';
import Menu from './interfaces/Menu';

function App() {
  return (
    <div className="App">
      <div>
        <Nav />

        <div className='container-fluid'>
          <div className='row'>
            <Menu />

            {/* <main role='main' className='col-md-9 ml-sm-auto col-lg-10 px-md-4'>
              {props.children}
            </main> */}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
