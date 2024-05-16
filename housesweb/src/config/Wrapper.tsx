import React, { PropsWithChildren } from 'react';
import Nav from '../interfaces/Nav';
import Menu from '../interfaces/Menu';

const Wrapper = (props: PropsWithChildren<any>) => {
    return (
        <div>
            <Nav />

            <div className='container-fluid'>
                <div className='row'>
                    <div className='col-2'>
                        <Menu />
                    </div>

                    <div className='col-10'>
                        <main role='main' className='col-md-9 col-lg-10 px-md-4 w-100'>
                            {props.children}
                        </main>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Wrapper;