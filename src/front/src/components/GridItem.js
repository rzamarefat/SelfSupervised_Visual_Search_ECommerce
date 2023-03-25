import React from 'react'
import { useDispatch } from 'react-redux'
import { setFocusedImage, setRecoms } from '../redux/actions'
import {useNavigate} from 'react-router-dom';
import axios from 'axios'

const GridItem = ({img}) => {
    const dispatch = useDispatch()
    const navigate = useNavigate();

    const handleClick = (img) => {
        dispatch(setFocusedImage(img.id))

        const body = JSON.stringify({
            "id": img.id
        }) 
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        }
        
        axios.post(`http://127.0.0.1:8000/item`, body, config)
        .then(res => {
            console.log(res)
            dispatch(setRecoms(res.data))
            navigate("/focus")

        })
        .catch(err => console.log(err))
    }

    return (
        <>
        <div className='grid-card shadow p-3 mb-5 bg-white'>
            <img 
                src={`data:image/jpeg;base64,${img.image}`} 
                // src={test_img} 
                className="grid-card-image" 
                onClick={() => handleClick(img)}
            />
        </div>
        </>
    )
}

export default GridItem