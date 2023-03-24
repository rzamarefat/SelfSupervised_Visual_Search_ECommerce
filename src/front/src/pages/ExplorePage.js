import GridView from '../components/GridView'
import Navbar from '../components/GridView'


const ExplorePage = () => {
    return (
        <>
            <div className='container'>
                <row className="">
                    <div className='col d-flex align-items-center justify-content-center flex-column'>
                        <div className='p-5'>
                            <h1>Explore</h1>    
                        </div>
                        <hr/>
                        <GridView/>
                    </div>
                </row>
            </div>
            
            
        </>
    )
}

export default ExplorePage