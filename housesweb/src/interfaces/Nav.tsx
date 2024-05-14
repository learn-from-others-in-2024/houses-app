import React from 'react';

const Nav = () => {
    return (
        <nav className='navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-1 shadow'>
            <a className='navbar-brand col-md-3 col-lg-2 mr-0 px-3' href='#'>
                Houses App
            </a>
            <button
                className='navbar-toggler position-absolute d-md-none collapsed'
                type='button'
                data-toggle='collapse'
                data-target='#sidebarMenu'
                aria-controls='sidebarMenu'
                aria-expanded='false'
                aria-label='Toggle navigation'
            >
                <span className='navbar-toggler-icon'></span>
            </button>
            <input
                className='form-control form-control-light w-100'
                type='text'
                placeholder='Search'
                aria-label='Search'
            />
            <ul className='navbar-nav px-3'>
                <li className='nav-item text-nowrap'>
                    <a className='nav-link' href='#'>
                        Sign out
                    </a>
                </li>
            </ul>
        </nav>
    );
};

export default Nav;