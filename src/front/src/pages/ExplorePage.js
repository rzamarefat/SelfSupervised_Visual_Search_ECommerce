import { useEffect } from 'react'
import {useDispatch, useSelector} from 'react-redux'
import GridView from '../components/GridView'
import Navbar from '../components/GridView'
import axios from 'axios'
import { putImages } from '../redux/actions'
import Loader from '../components/Loader'
import {useNavigate} from 'react-router-dom';


const ExplorePage = () => {
    const dispatch = useDispatch()
    const images = useSelector(state => state.images[0])
    const embApproach = useSelector(state => state.embApproach)
    const navigate = useNavigate();

    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/explore")
        .then(res => {
            console.log(res)
            dispatch(putImages([res.data.images]))

        })
        .catch(err => console.log(err))
    }, [embApproach])
        

    return (
        <>
            <div className='container'>
                <row className="">
                    <div className='col d-flex align-items-center justify-content-center flex-column'>
                        <div className='p-5'>
                            <h1>Explore</h1>    
                        </div>
                        <div>
                            <div className="btn bg-dark text-light" onClick={() => navigate("/config")}>Configuration</div>
                        </div>
                        <hr/>
                        {!images && <Loader/>}
                        {images && <GridView images={images}/>}
                    </div>
                </row>
            </div>

            
            
            
            
        </>
    )
}

export default ExplorePage