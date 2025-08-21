import { combineReducers } from 'redux';
import countReducer from './countReducer.js';

const allReducers = combineReducers({
  countReducer,
});

export default allReducers;