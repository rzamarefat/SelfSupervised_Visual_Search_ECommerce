import { useState } from "react"
import GridItem from "../components/GridItem"

const FocusPage = () => {
    const recoms = useState(state => state.recoms)
    const focusedItem = useState(state => state.focusedItem)

    return (
        <>
            {recoms && <div className='container'>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col-sm-5 d-flex align-items-center justify-content-center flex-column'>
                        <GridItem img={focusedItem}/>
                    </div>    
                </div>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col d-flex align-items-center justify-content-center'>
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