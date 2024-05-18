import React, { SyntheticEvent, useEffect, useState, } from 'react';
import Wrapper from './Wrapper';
import { useNavigate, useParams } from 'react-router-dom';
import { House } from '../interfaces/house';

const HousesUpdate = () => {
    const { id } = useParams<{ id: string }>();
    const [name, setName] = useState('');
    const [image, setImage] = useState('');
    const [description, setDescription] = useState('');
    const [redirect, setRedirect] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        if (redirect) {
            navigate('/config/houses');
        }
    }, [redirect, navigate]);

    useEffect(() => {
        console.log(id); // Check if the id is correctly retrieved
        (async () => {
            const response = await fetch(
                `http://localhost:8000/api/houses/${id}`
            );

            const house: House = await response.json();

            setName(house.name);
            setImage(house.image);
            setDescription(house.description);
        })();
    }, [id]);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch(`http://localhost:8000/api/houses/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                image,
                description,
            }),
        });

        setRedirect(true);
    };

    const handleCancel = () => {
        navigate('/config/houses');
    };

    return (
        <Wrapper>
            <div className='mt-4 rounded shadow border border-light border-1 p-4'>
                <h1>Edit House</h1>
                <form onSubmit={submit}>
                    <div className='form-group mb-2'>
                        <label>Name</label>
                        <input placeholder='Name' type='text' className='form-control' name='name' value={name} onChange={(e) => setName(e.target.value)} />
                    </div>
                    <div className='form-group mb-2'>
                        <label>Image</label>
                        <input placeholder='Name' type='text' className='form-control' name='image' value={image} onChange={(e) => setImage(e.target.value)} />
                    </div>
                    <div className='form-group mb-2'>
                        <label>Description</label>
                        <input placeholder='Description' type='text' className='form-control' name='description' value={description} onChange={(e) => setDescription(e.target.value)} />
                    </div>
                    <div className='mt-3'>
                        <button className='btn btn-outline-warning me-2'>Update</button>
                        <button type='button' className='btn btn-outline-secondary' onClick={handleCancel}>Cancel</button>
                    </div>
                </form>
            </div>
        </Wrapper>
    );
};

export default HousesUpdate;