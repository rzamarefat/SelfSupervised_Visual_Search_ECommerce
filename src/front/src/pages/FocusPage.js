import GridItem from "../components/GridItem"

const FocusPage = () => {

    return (
        <>
            <div className='container'>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col-sm-5 d-flex align-items-center justify-content-center flex-column'>
                        <GridItem/>
                    </div>    
                </div>
                <div className="row  h-100 d-flex align-items-center justify-content-center">
                    <div className='col d-flex align-items-center justify-content-center'>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                        <GridItem/>
                    </div>    
                </div>
            </div>
        </>
    )
}

export default FocusPage