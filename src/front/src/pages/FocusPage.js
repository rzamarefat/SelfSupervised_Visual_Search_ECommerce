import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import GridItem from "../components/GridItem"
import { setRecoms } from "../redux/actions"
import axios from 'axios'

const FocusPage = () => {
    const dispatch = useDispatch()
    const recoms = useSelector(state => state.recoms)
    const focusedItem = useSelector(state => state.focusedItem)

    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/item")
        .then(res => {
            console.log(res)
            dispatch(setRecoms([res.data.images]))

        })
        .catch(err => console.log(err))
    }, [])

    return (
        <>
            {recoms && <div className='container'>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col-sm-5 d-flex align-items-center justify-content-center flex-column'>
                        <GridItem img={focusedItem}/>
                        {console.log()}
                    </div>    
                </div>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col d-flex align-items-center justify-content-center'>
                        {recoms.map(rec => {
                            console.log("LLLLL", rec)
                            return (<GridItem img={rec}/>)
                        })}
                        
                    </div>    
                </div>
            </div>}
        </>
    )
}

export default FocusPage