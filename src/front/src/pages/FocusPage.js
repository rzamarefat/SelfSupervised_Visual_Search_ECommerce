const PageB = () => {
    return (
        <>
            <div className='container'>
                <row className="">
                    <div className='col d-flex align-items-center justify-content-center flex-column'>
                        <div className='p-5'>
                            <h1>Explore</h1>    
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

export default PageB