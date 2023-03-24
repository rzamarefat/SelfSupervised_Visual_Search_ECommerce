import React from 'react'

const GridItem = () => {
    const cardImage = require('./25111.jpg')

    return (
        <>
        <div className='grid-card shadow p-3 mb-5 bg-white'>
            <img src={cardImage} className="grid-card-image"/>
            <h1>He</h1>
        </div>
        </>
    )
}

export default GridItem