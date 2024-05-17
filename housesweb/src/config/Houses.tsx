import React, { useEffect, useState } from 'react';
import Wrapper from './Wrapper';
import { House } from '../interfaces/house';
import { Link } from 'react-router-dom';

const Houses = () => {
    const [houses, setHouses] = useState([]);

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:8000/api/houses');

            const data = await response.json();

            setHouses(data);
        })();
    }, []);

    const del = async (id: number) => {
        if (window.confirm('Are you sure you want to delete this house?')) {
            await fetch(`http://localhost:8000/api/houses/${id}`, {
                method: 'DELETE',
            });

            setHouses(houses.filter((h: House) => h.id !== id));
        }
    };

    return (
        <Wrapper>
            <div className='pt-3 pb-2 mb-3 border-bottom'>
                <div className='btn-toolbar mb-2 mb-md-0'>
                    <Link to='/config/houses/create' className='btn btn-sm btn-outline-success'>
                        Add
                    </Link>
                </div>
            </div>

            <div className='table-responsive'>
                <table className='table table-striped table-sm'>
                    <thead>
                        <tr>
                            <th>Number</th>
                            <th>Image</th>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Likes</th>
                            <th>Checks</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {houses.map((h: House) => {
                            return (
                                <tr key={h.id}>
                                    <td>{h.id}</td>
                                    <td>
                                        <img src={h.image} height='180' alt={h.name} />
                                    </td>
                                    <td>{h.name}</td>
                                    <td>{h.description}</td>
                                    <td>{h.likes}</td>
                                    <td>{h.checks}</td>
                                    <td>
                                        <div className='btn-group mr-2'>
                                            <Link to={`/config/houses/${h.id}/update`} className='btn btn-sm btn-outline-warning'>
                                                Update
                                            </Link>
                                            <button className='btn btn-sm btn-outline-danger' onClick={() => del(h.id)}>
                                                Delete
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>
        </Wrapper>
    );
};

export default Houses;