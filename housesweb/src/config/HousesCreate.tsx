import React, { SyntheticEvent, useState, useEffect } from 'react';
import Wrapper from './Wrapper';
import { useNavigate } from 'react-router-dom';

const HousesCreate = () => {
    const [name, setName] = useState('');
    const [image, setImage] = useState('');
    const [description, setDescription] = useState('');
    const [redirect, setRedirect] = useState(false);
    const [errors, setErrors] = useState<{ [key: string]: string }>({});
    const navigate = useNavigate();

    useEffect(() => {
        if (redirect) {
            navigate('/config/houses');
        }
    }, [redirect, navigate]);

    const validateForm = () => {
        let formErrors: { [key: string]: string } = {};
        if (!name) formErrors.name = "Name is required";
        if (!image) formErrors.image = "Image URL is required";
        if (!description) formErrors.description = "Description is required";

        setErrors(formErrors);

        return Object.keys(formErrors).length === 0;
    };

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        if (!validateForm()) {
            return;
        }

        await fetch('http://localhost:8000/api/houses', {
            method: 'POST',
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
                <h1>Add New House</h1>
                <form onSubmit={submit}>
                    <div className='form-group mb-2'>
                        <label>Name</label>
                        <input placeholder='Name' type='text' className='form-control' name='name' onChange={(e) => setName(e.target.value)} />
                        {errors.name && <span className="text-danger">{errors.name}</span>}
                    </div>
                    <div className='form-group mb-2'>
                        <label>Image</label>
                        <input placeholder='Image' type='text' className='form-control' name='image' onChange={(e) => setImage(e.target.value)} />
                        {errors.image && <span className="text-danger">{errors.image}</span>}
                    </div>
                    <div className='form-group mb-2'>
                        <label>Description</label>
                        <input placeholder='Description' type='text' className='form-control' name='description' onChange={(e) => setDescription(e.target.value)} />
                        {errors.description && <span className="text-danger">{errors.description}</span>}
                    </div>
                    <div className='mt-3'>
                        <button type='submit' className='btn btn-outline-success me-2'>Save</button>
                        <button type='button' className='btn btn-outline-secondary' onClick={handleCancel}>Cancel</button>
                    </div>
                </form>
            </div>
        </Wrapper>
    );
};

export default HousesCreate;