import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import GridItem from "../components/GridItem"
import { setRecoms } from "../redux/actions"
import axios from 'axios'

const FocusPage = () => {
    const dispatch = useDispatch()
    const recoms = useSelector(state => state.recoms[0])
    const focusedItem = useSelector(state => state.focusedItem)
    const focusedItemImage = useSelector(state => state.focusedItemImage)


    useEffect(()=>{
        console.log("http://127.0.0.1:8000/item")
        axios.get("http://127.0.0.1:8000/item")
        .then(res => {
            console.log(res)
            dispatch(setRecoms([res.data.images]))

        })
        .catch(err => console.log(err))
    }, [focusedItem])

    return (
        <>
            {recoms && <div className='container'>
                <div className="row d-flex align-items-center justify-content-center">
                    <div className='col-sm-5 d-flex align-items-center justify-content-center flex-column'>
                    <img 
                        src={`data:image/jpeg;base64,${focusedItemImage}`} 
                        className="grid-card-image" 
                    />

                    </div>    
                </div>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col-sm-5'>
                        {recoms.map(rec => {
                            return (<GridItem img={rec}/>)
                        })}
                        
                    </div>    
                </div>
            </div>}
        </>
    )
}

export default FocusPage