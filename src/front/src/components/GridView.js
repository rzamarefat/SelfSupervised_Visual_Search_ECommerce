import React from 'react'
import GridItem from './GridItem'

const GridView = ({images}) => {
  return (
    <>
        <div className='row'>
            {images.map(img => {
                return (
                    <div className='col-sm-3'>
                        <GridItem img={img}/>
                    </div>
                )
            })}
            
        </div>

        
    </>
    
  )
}

export default GridView