import React from 'react'

function Menu() {
    return (
        <nav id='sidebarMenu' className='col-md-3 col-lg-2 d-md-block bg-secondary sidebar collapse'>
            <div className='sidebar-sticky pt-3'>
                <ul className='nav flex-column'>
                    <li className='nav-item'>
                        <a className='nav-link active text-white' href='/config/houses'>
                            Houses
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Menu