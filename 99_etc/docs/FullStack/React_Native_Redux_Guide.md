# React Native Redux Guide

## Redux 기본 개념

### 주요 개념

1. **Action (액션)**
   - 상태에 어떤 변화가 필요할 때, 액션이 발생합니다.
   - 액션 객체는 `type` 필드를 필수로 포함하며, 추가적으로 필요한 데이터를 포함할 수 있습니다.

2. **Action Creator (액션 생성 함수)**
   - 액션 객체를 생성하는 함수입니다.
   ```javascript
   function increment() {
     return { type: 'INCREMENT' };
   }
   ```

3. **Reducer (리듀서)**
   - 현재 상태와 액션 객체를 받아 새로운 상태를 반환하는 함수입니다.
   ```javascript
   function reducer(state, action) {
     switch (action.type) {
       case 'INCREMENT':
         return { count: state.count + 1 };
       default:
         return state;
     }
   }
   ```

4. **Store (스토어)**
   - 애플리케이션의 상태를 관리하는 객체입니다.
   - 리듀서를 등록하고, 상태를 구독하거나 액션을 디스패치할 수 있습니다.

5. **Dispatch (디스패치)**
   - 액션을 스토어에 전달하는 함수입니다.
   ```javascript
   store.dispatch({ type: 'INCREMENT' });
   ```

6. **Subscribe (구독)**
   - 상태가 변경될 때마다 특정 함수를 실행하도록 등록합니다.
   ```javascript
   store.subscribe(() => console.log(store.getState()));
   ```

---

## React Native Redux 프로젝트 예제

### 프로젝트 생성 및 설정

1. 프로젝트 생성
   ```bash
   npx react-native init ReduxDemo
   cd ReduxDemo
   ```

2. 필요한 라이브러리 설치
   ```bash
   npm install redux react-redux native-base @expo/vector-icons
   ```

### Redux Reducer 작성

#### reducers/countReducer.js
```javascript
const initialState = {
  count: 0
};

export const INCREMENT = 'Increment';
export const DECREMENT = 'Decrement';

export function increment() {
  return { type: INCREMENT };
}

export function decrement() {
  return { type: DECREMENT };
}

function reducer(state = initialState, action) {
  switch (action.type) {
    case INCREMENT:
      return { count: state.count + 1 };
    case DECREMENT:
      return { count: state.count - 1 };
    default:
      return state;
  }
}

export default reducer;
```

#### reducers/index.js
```javascript
import { combineReducers } from 'redux';
import countReducer from './countReducer';

const allReducers = combineReducers({
  countReducer
});

export default allReducers;
```

### React Native 컴포넌트 작성

#### components/Counter.js
```javascript
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Container, Content, Text, Card, Header, Body, Button, Title, CardItem } from 'native-base';
import { increment, decrement } from '../reducers/countReducer';

class Counter extends Component {
  render() {
    return (
      <Container>
        <Header>
          <Body>
            <Title>Redux Counter</Title>
          </Body>
        </Header>
        <Content padder>
          <Card>
            <CardItem>
              <Text>{this.props.state.count}</Text>
            </CardItem>
          </Card>
          <Button full onPress={() => this.props.increment()} style={{ marginVertical: 10 }}>
            <Text>Increment</Text>
          </Button>
          <Button full dark bordered onPress={() => this.props.decrement()}>
            <Text>Decrement</Text>
          </Button>
        </Content>
      </Container>
    );
  }
}

function mapStateToProps(state) {
  return {
    state: state.countReducer
  };
}

function matchDispatchToProps(dispatch) {
  return bindActionCreators({
    increment,
    decrement
  }, dispatch);
}

export default connect(mapStateToProps, matchDispatchToProps)(Counter);
```

### App.js
```javascript
import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import allReducers from './reducers';
import Counter from './components/Counter';

const store = createStore(allReducers);

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Counter />
      </Provider>
    );
  }
}
```

---

## 실행 방법

1. 프로젝트 디렉토리로 이동
   ```bash
   cd ReduxDemo
   ```

2. 애플리케이션 실행
   ```bash
   npx react-native run-android
   ```

3. 결과 확인
   - Increment 버튼을 누르면 카운트가 증가합니다.
   - Decrement 버튼을 누르면 카운트가 감소합니다.
