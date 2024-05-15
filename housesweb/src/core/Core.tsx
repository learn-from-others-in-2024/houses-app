import React, { useEffect, useState } from 'react';
import { House } from '../interfaces/house';
import Wrapper from '../config/Wrapper';

const Core = () => {
    const [houses, setHouses] = useState([] as House[]);

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:5005/api/houses');

            const data = await response.json();

            setHouses(data);
        })();
    }, []);

    const like = async (id: number) => {
        await fetch(`http://localhost:5005/api/houses/${id}/like`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });

        setHouses(
            houses.map((h: House) => {
                if (h.id === id) {
                    h.likes++;
                }

                return h;
            })
        );
    };

    const check = async (id: number) => {
        await fetch(`http://localhost:5005/api/houses/${id}/check`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });

        setHouses(
            houses.map((h: House) => {
                if (h.id === id) {
                    h.checks++;
                }

                return h;
            })
        );
    };

    return (
        <Wrapper>
            <main role='main'>
                <div className='album py-5 bg-light'>
                    <div className='container'>
                        <div className='row'>
                            {houses.map((h: House) => {
                                return (
                                    <div className='col-md-4' key={h.id}>
                                        <div className='card mb-4 shadow-sm'>
                                            <img src={h.image} height='180' alt={h.name} />
                                            <div className='card-body'>
                                                <p className='card-text'><b>{h.name}</b></p>
                                                <p className='card-text'>{h.description}</p>
                                                <div className='d-flex justify-content-between align-items-center'>
                                                    <div className='btn-group'>
                                                        <button
                                                            type='button'
                                                            className='btn btn-sm btn-outline-secondary'
                                                            onClick={() => like(h.id)}
                                                        >
                                                            Like
                                                        </button>
                                                    </div>
                                                    <div className='btn-group'>
                                                        <button
                                                            type='button'
                                                            className='btn btn-sm btn-outline-secondary'
                                                            onClick={() => check(h.id)}
                                                        >
                                                            Check
                                                        </button>
                                                    </div>
                                                    <small className='text-muted'>{h.likes} likes</small>
                                                    <small className='text-muted'>{h.checks} checks</small>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>
            </main>
        </Wrapper>
    );
};

export default Core;