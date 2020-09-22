import React from 'react'
import './Circles.css'

const Circles = (props) => {
    return (
        <div className="Circles">
            {props.circleNo.map((circle, idx) =>
            <div
                className={props.circleIdx === idx ? 'selected' : ''}
                onClick={() => props.handleCircleClick(idx)}
                >{idx+1}
            </div>
            )}
        </div>
    )
}

export default Circles