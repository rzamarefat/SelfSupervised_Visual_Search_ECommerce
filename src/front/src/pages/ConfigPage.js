import React from 'react'
import { useSelector, useDispatch } from 'react-redux';
import {useNavigate} from 'react-router-dom';
import { setEmbApproach } from '../redux/actions';

const ConfigPage = () => {
    const embApproach = useSelector(state => state.embApproach)
    const navigate = useNavigate();
    const dispatch = useDispatch()

    const handleApplyClick = () => {
        navigate("/")
    }
    
  return (
    <div className='container'>
        <row className="">
            <div className='col d-flex align-items-center justify-content-center flex-column'>
                <div className='p-5'>
                    <h1>Configuration</h1>
                </div>
                <div className='p-5 border'>
                    <h4>Choose Self-Supervised approach</h4>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" onChange={() => dispatch(setEmbApproach("SIMCLR"))} checked={embApproach === "SIMCLR"}/>
                        <label class="form-check-label" for="flexRadioDefault1">
                            SimCLR
                        </label>
                    </div>

                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" onChange={() => dispatch(setEmbApproach("BYOL"))} checked={embApproach === "BYOL"}/>
                        <label class="form-check-label" for="flexRadioDefault1">
                            BYOL
                        </label>
                    </div>
                </div>
                <div className='btn bg-dark text-light w-100 mt-5' onClick={() => handleApplyClick()}>Apply</div>
                <hr/>
            </div>
        </row>
    </div>
  )
}

export default ConfigPage