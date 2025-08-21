# React Example Guide

## React 기본 예제

### HTML 예제

#### 첫 번째 예제: hello.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
```

#### 두 번째 예제: 이벤트 처리

##### event1.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
```

##### event2.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
```

##### event3.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
```

### React 프로젝트 생성 및 실행

1. Node.js 설치
2. Create React App 설치
   ```bash
   npx create-react-app hello-react
   cd hello-react
   npm install
   yarn start
   ```

3. 필요한 라이브러리 설치
   ```bash
   yarn add react-router-dom axios bootstrap
   ```

### React 컴포넌트 예제

#### index.js
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

#### App.js
```javascript
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Hello, React!</p>
      </header>
    </div>
  );
}

export default App;
```

#### App1.js (클래스 컴포넌트)
```javascript
import React from 'react';

class App1 extends React.Component {
  render() {
    return <h1>클래스 컴포넌트 예제</h1>;
  }
}

export default App1;
```

#### App2.js (함수형 컴포넌트)
```javascript
import React, { useState } from 'react';

function App2() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}

export default App2;
```

---

## React Native 예제

### React Native 프로젝트 생성 및 실행

1. 프로젝트 생성
   ```bash
   npx react-native init MyApp3
   cd MyApp3
   npx react-native run-android
   ```

2. 디버깅
   - 에뮬레이터에서 `Ctrl + M`을 눌러 디버그 메뉴를 엽니다.
   - 크롬 브라우저에서 디버깅: [http://localhost:8081/debugger-ui/](http://localhost:8081/debugger-ui/)

### React Native 기본 컴포넌트

#### App.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

class App extends React.Component {
  render() {
    return (
      <View>
        <Text>This is my second android app</Text>
      </View>
    );
  }
}

export default App;
```

---

## Redux CRUD 예제

### 프로젝트 생성 및 설정

1. 프로젝트 생성
   ```bash
   npx create-react-app crud-redux
   cd crud-redux
   npm install redux react-redux react-router-dom bootstrap axios redux-thunk
   ```

2. 기본 파일 설정

#### index.js
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import postReducer from './reducers/postReducer';
import App from './App';

const store = createStore(postReducer);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

#### App.js
```javascript
import React from 'react';
import PostForm from './PostForm';
import AllPost from './AllPost';

function App() {
  return (
    <div>
      <PostForm />
      <AllPost />
    </div>
  );
}

export default App;
```

---

## Vite + React 예제

### Vite 프로젝트 생성

1. 프로젝트 생성
   ```bash
   npm create vite@latest myhome_vite
   cd myhome_vite
   npm install
   npm run dev
   ```

2. 라우터 및 추가 라이브러리 설치
   ```bash
   npm i react-router-dom react-bootstrap bootstrap axios
   ```
