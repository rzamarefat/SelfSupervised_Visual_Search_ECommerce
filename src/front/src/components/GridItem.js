import React from 'react'

const GridItem = ({img}) => {
    // const cardImage = require('./25111.jpg')

    return (
        <>
        <div className='grid-card shadow p-3 mb-5 bg-white'>
            <img src={`data:image/jpeg;base64,${img}`} className="grid-card-image"/>
        </div>
        </>
    )
}

export default GridItem