import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import allReducers from './reducers';
import Counter from './components/counter.js';

const store = createStore(allReducers);

export default class App extends Component{
  render(){
    return(
      <Provider store={store}>
        <Counter />
      </Provider>
    );
  }
}