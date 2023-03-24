import { useEffect } from 'react'
import {useDispatch, useSelector} from 'react-redux'
import GridView from '../components/GridView'
import Navbar from '../components/GridView'
import axios from 'axios'
import { putImages } from '../redux/actions'



const ExplorePage = () => {
    const dispatch = useDispatch()
    const images = useSelector(state => state.images[0])

    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/explore")
        .then(res => {
            console.log(res)
            console.log("========")
            // console.log(res.data.images)
            console.log(images)
            console.log("========")
            dispatch(putImages([res.data.images]))

        })
        .catch(err => console.log(err))
    }, [])
        

    return (
        <>
            <div className='container'>
                <row className="">
                    <div className='col d-flex align-items-center justify-content-center flex-column'>
                        <div className='p-5'>
                            <h1>Explore</h1>    
                        </div>
                        <hr/>
                        {images && <GridView images={images}/>}
                    </div>
                </row>
            </div>
            
            
        </>
    )
}

export default ExplorePage