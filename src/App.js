import React, { Component } from 'react';
import './App.css';
import CircleSelector from './Components/CircleSelector/CircleSelector'
import Circles from './Components/Circles/Circles'

const circleNo = ['0', '1', '2', '3']

class App extends Component {
  state = {
    circleIdx: 0
  }

  handleCircleClick = (idx) => {
    this.setState({ circleIdx: idx })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">UNIT 4 FINAL ASSESSMENT</header>
        <main>
          <CircleSelector 
          circleNo={circleNo}
          circleIdx={this.state.circleIdx}
          handleCircleClick={this.handleCircleClick}
          />
          <Circles 
          circleNo={circleNo}
          circleIdx={this.state.circleIdx}
          handleCircleClick={this.handleCircleClick}
          />
        </main>
      </div>
    );
  }
}

export default App;