import React from 'react'
import { useSelector } from 'react-redux'
import GridItem from './GridItem'
import Loader from './Loader'

const GridView = ({images}) => {

    return (
        <>
            
            <div className='row'>
                {images.map(img => {
                    return (
                        <>
                            {console.log("inside explore", img)}
                            <div className='col-sm-3'>
                                <GridItem img={img}/>
                            </div>
                            
                        </>
                        

                    )
                })}
                
            </div>

            
        </>
        
    )
}

export default GridView