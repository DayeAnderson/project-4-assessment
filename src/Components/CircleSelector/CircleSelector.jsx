import React from 'react'
import './CircleSelector.css'

const CircleSelector = (props) => {
    return (
        <div className="CircleSelector">
            {props.circleNo.map((circle, idx) =>
            <button
            className={props.circleIdx === idx ? 'selected' : ''}
            onClick={() => props.handleCircleClick(idx)}
            >
                {props.circleIdx === idx ? `Circle ${idx+1} Selected` : `Select Circle ${idx+1}`}
            </button>
            )}
        </div>
    )
}

export default CircleSelector