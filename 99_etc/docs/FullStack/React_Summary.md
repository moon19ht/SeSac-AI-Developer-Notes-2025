# React.js 완벽 가이드

이 문서는 React의 기본 개념부터 실제 프로젝트 설정, 그리고 백엔드 연동에 이르기까지 포괄적인 내용을 다루는 가이드입니다.

---

## 목차

1.  [React란?](#1-react란)
    -   [특징](#특징)
    -   [React 사용 이유: SPA](#react-사용-이유-spa---single-page-application)
2.  [React 핵심 개념](#2-react-핵심-개념)
    -   [Virtual DOM](#virtual-dom)
    -   [JSX (JavaScript XML)](#jsx-javascript-xml)
    -   [컴포넌트 (Component)](#컴포넌트-component)
    -   [Props와 State](#props와-state)
    -   [이벤트 처리 (Event Handling)](#이벤트-처리-event-handling)
3.  [React 개발 환경 설정](#3-react-개발-환경-설정)
    -   [Node.js와 Yarn 설치](#nodejs와-yarn-설치)
    -   [Create React App으로 프로젝트 생성](#create-react-app으로-프로젝트-생성)
4.  [실전 예제: 틱택토 게임 만들기](#4-실전-예제-틱택토-게임-만들기)
    -   [컴포넌트 구조](#컴포넌트-구조)
    -   [State 관리와 불변성](#state-관리와-불변성)
    -   [시간 여행 기능 추가](#시간-여행-기능-추가)
5.  [React Hooks](#5-react-hooks)
    -   [State Hook: `useState`](#state-hook-usestate)
    -   [Effect Hook: `useEffect`](#effect-hook-useeffect)
6.  [React Router를 이용한 라우팅](#6-react-router를-이용한-라우팅)
7.  [백엔드 연동](#7-백엔드-연동)
    -   [MySQL 연동](#mysql-연동)
    -   [MongoDB 연동](#mongodb-연동)
    -   [Spring Boot 연동](#spring-boot-연동)

---

## 1. React란?

React는 사용자 인터페이스(UI)를 만들기 위한 JavaScript 라이브러리입니다. Facebook과 Instagram에서 개발한 오픈소스 프로젝트로, 웹 애플리케이션 개발에 널리 사용됩니다.

### 특징

-   **선언형 (Declarative):** 상호작용이 많은 UI를 만들 때 생기는 어려움을 줄여줍니다. 애플리케이션의 각 상태에 대해 간단한 뷰만 설계하면, 데이터가 변경될 때 React가 효율적으로 적절한 컴포넌트만 갱신하고 렌더링합니다.
-   **컴포넌트 기반 (Component-Based):** 스스로 상태를 관리하는 캡슐화된 컴포넌트를 만듭니다. 이를 통해 UI를 독립적인 여러 조각으로 나누어 개발하고 재사용할 수 있습니다.
-   **빠른 속도:** Virtual DOM을 사용하여 데이터가 변경된 컴포넌트만 효율적으로 다시 렌더링하므로 빠른 성능을 제공합니다.

### React 사용 이유: SPA (Single Page Application)

Naver Vibe, Instagram과 같은 최신 웹사이트들은 페이지 전환 시 새로고침 없이 부드럽게 동작합니다. 이러한 애플리케이션을 **SPA(Single Page Application)**라고 합니다.

SPA는 최초에 한 번만 전체 페이지를 로드하고, 이후에는 사용자의 요청에 따라 필요한 데이터만 서버에서 비동기적으로(Ajax) 불러와 동적으로 페이지를 업데이트합니다. 이를 통해 사용자 경험이 향상되고 애플리케이션 속도가 빨라집니다.

-   **장점:** 초기 로딩 후의 처리 속도가 빠르고, 부드러운 사용자 경험을 제공합니다.
-   **단점:** 앱의 규모가 커지면 초기 로딩 시간이 길어질 수 있으며, 검색 엔진 최적화(SEO)가 어려울 수 있습니다.

---

## 2. React 핵심 개념

### Virtual DOM

Virtual DOM(가상 DOM)은 실제 브라우저 DOM의 사본을 메모리에 저장하는 개념입니다. 상태가 변경되면 React는 다음 두 단계를 거칩니다.

1.  **비교 (Diffing):** 메모리에 있는 Virtual DOM의 이전 상태와 변경된 상태를 비교하여 차이점을 찾아냅니다.
2.  **최소한의 업데이트:** 변경된 부분만 실제 DOM에 한 번에 반영합니다.

이 과정을 통해 불필요한 DOM 조작을 최소화하여 웹 애플리케이션의 성능을 최적화합니다.

### JSX (JavaScript XML)

JSX는 JavaScript를 확장한 문법으로, JavaScript 코드 안에서 HTML과 유사한 형태로 UI를 작성할 수 있게 해줍니다.

```jsx
function App() {
  const name = "React";
  return (
    <div>
      <h1>Hello, {name}!</h1>
    </div>
  );
}
```

-   브라우저는 JSX를 직접 이해하지 못하므로, Babel과 같은 트랜스파일러를 통해 `React.createElement()` 함수 호출로 변환됩니다.
-   JSX 내에서 JavaScript 표현식을 사용하려면 중괄호 `{}`로 감싸야 합니다.
-   CSS 스타일은 camelCase를 사용하는 JavaScript 객체 형태로 적용합니다.
-   HTML의 `class` 속성은 JSX에서 `className`으로 사용합니다.

### 컴포넌트 (Component)

컴포넌트는 React 앱을 구성하는 독립적이고 재사용 가능한 UI 조각입니다. 컴포넌트는 크게 두 가지 형태로 작성할 수 있습니다.

-   **함수형 컴포넌트 (Functional Component):** JavaScript 함수 형태로 작성되며, props를 인자로 받아 JSX를 반환합니다. React 16.8 버전 이후 **Hooks**가 도입되면서 상태 관리와 라이프사이클 기능을 사용할 수 있게 되어 현재 가장 널리 사용됩니다.

    ```jsx
    function Welcome(props) {
      return <h1>Hello, {props.name}</h1>;
    }
    ```

-   **클래스형 컴포넌트 (Class Component):** ES6 클래스 문법으로 작성되며, `React.Component`를 상속받습니다. `render()` 메서드에서 JSX를 반환하며, `state`와 라이프사이클 메서드를 가집니다.

    ```jsx
    class Welcome extends React.Component {
      render() {
        return <h1>Hello, {this.props.name}</h1>;
      }
    }
    ```

### Props와 State

-   **Props (Properties):** 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때 사용되는 읽기 전용(immutable) 데이터입니다.

-   **State:** 컴포넌트 내부에서 관리되는 동적인 데이터입니다. `useState` Hook(함수형)이나 `this.setState`(클래스형)를 통해 상태를 변경하면 컴포넌트가 다시 렌더링됩니다.

### 이벤트 처리 (Event Handling)

React의 이벤트는 HTML과 유사하지만, 몇 가지 차이점이 있습니다.

-   이벤트 이름은 camelCase(`onClick`, `onChange`)를 사용합니다.
-   이벤트 핸들러로는 문자열이 아닌 함수를 전달합니다.

```jsx
function MyButton() {
  function handleClick() {
    alert('Button clicked!');
  }

  return (
    <button onClick={handleClick}>
      Click me
    </button>
  );
}
```

React는 DOM 이벤트를 감싸는 **SyntheticEvent** 객체를 사용하여 브라우저 간의 호환성을 보장합니다.

---

## 3. React 개발 환경 설정

### Node.js와 Yarn 설치

React 개발을 위해서는 JavaScript 런타임인 **Node.js**가 필요합니다. Node.js를 설치하면 패키지 매니저인 **npm**이 함께 설치됩니다.

-   [Node.js 공식 홈페이지](https://nodejs.org/ko/)에서 안정화 버전(LTS)을 설치합니다.

**Yarn**은 npm보다 빠르고 효율적인 캐싱 시스템을 제공하는 패키지 매니저입니다. npm을 통해 전역으로 설치할 수 있습니다.

```bash
npm install -g yarn
```

### Create React App으로 프로젝트 생성

**Create React App**은 React 프로젝트를 쉽게 생성할 수 있도록 도와주는 공식 도구입니다.

1.  **프로젝트 생성:**
    ```bash
    npx create-react-app my-react-app
    ```

2.  **프로젝트 폴더로 이동:**
    ```bash
    cd my-react-app
    ```

3.  **개발 서버 실행:**
    ```bash
    yarn start
    ```

이제 `http://localhost:3000`에서 실행 중인 React 애플리케이션을 확인할 수 있습니다.

---

## 4. 실전 예제: 틱택토 게임 만들기

(이 섹션은 제공된 `react.md`의 틱택토 예제 내용을 요약 및 재구성한 것입니다.)

틱택토 게임 예제를 통해 컴포넌트 간의 데이터 전달, state 관리, 불변성의 중요성을 배울 수 있습니다.

### 컴포넌트 구조

-   **Square:** 게임 판의 각 칸을 나타내는 버튼 컴포넌트.
-   **Board:** 9개의 Square 컴포넌트를 렌더링하고 게임의 상태를 관리하는 부모 컴포넌트.
-   **Game:** Board와 게임 정보(진행 상황, 시간 여행)를 렌더링하는 최상위 컴포넌트.

### State 관리와 불변성

게임의 상태(각 칸의 값, 다음 차례 등)는 부모 컴포넌트인 `Board`에서 관리하는 것이 효율적입니다. 이를 **"State 끌어올리기(Lifting State Up)"**라고 합니다.

React에서는 상태를 직접 수정하는 대신, `slice()`와 같은 메서드를 사용하여 객체의 복사본을 만들고 그 복사본을 변경하는 **불변성**을 유지하는 것이 중요합니다. 불변성은 다음과 같은 장점을 가집니다.

-   **변화 감지 용이:** 객체의 참조가 달라졌는지 여부만으로 변화를 쉽게 감지할 수 있습니다.
-   **성능 최적화:** React가 언제 리렌더링할지 결정하는 데 도움을 줍니다.

### 시간 여행 기능 추가

게임의 각 단계를 기록하여 이전 상태로 돌아갈 수 있는 "시간 여행" 기능을 구현할 수 있습니다. 이를 위해 게임 상태의 `history`를 배열로 저장하고, 사용자가 특정 시점을 선택하면 해당 시점의 상태를 화면에 렌더링합니다.

---

## 5. React Hooks

React 16.8부터 도입된 Hooks는 함수형 컴포넌트에서 `state`와 라이프사이클 기능을 사용할 수 있게 해주는 함수들입니다.

### State Hook: `useState`

`useState`는 함수형 컴포넌트에서 `state`를 관리하게 해주는 Hook입니다.

```jsx
import React, { useState } from 'react';

function Counter() {
  // count라는 새 상태 변수를 선언하고, 초기값은 0입니다.
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### Effect Hook: `useEffect`

`useEffect`는 컴포넌트가 렌더링될 때마다 특정 작업을 수행하도록 설정할 수 있는 Hook입니다. 데이터 가져오기, 구독 설정, DOM 조작 등의 부수 효과(Side Effect)를 처리하는 데 사용됩니다.

-   `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`의 역할을 모두 수행할 수 있습니다.

---

## 6. React Router를 이용한 라우팅

React는 기본적으로 라우팅 기능을 제공하지 않으므로, `react-router-dom` 라이브러리를 사용하여 SPA에서 페이지 전환을 구현합니다.

1.  **라이브러리 설치:**
    ```bash
    npm install react-router-dom
    ```

2.  **라우터 설정:**
    `App.js` 파일에서 `BrowserRouter`, `Routes`, `Route` 컴포넌트를 사용하여 경로에 따라 다른 컴포넌트를 렌더링하도록 설정합니다.

    ```jsx
    import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
    import Home from './Home';
    import About from './About';

    function App() {
      return (
        <BrowserRouter>
          <nav>
            <Link to="/">Home</Link> | <Link to="/about">About</Link>
          </nav>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </BrowserRouter>
      );
    }
    ```

---

## 7. 백엔드 연동

(이 섹션은 제공된 `react.md`의 데이터베이스 및 서버 연동 내용을 요약한 것입니다.)

### MySQL 연동

-   MariaDB(MySQL 기반)를 설치하고, `mysql_install_db` 스크립트를 사용하여 데이터베이스를 설정합니다.
-   `CREATE DATABASE`, `GRANT` 명령어를 통해 데이터베이스와 사용자를 생성합니다.
-   HeidiSQL과 같은 GUI 도구를 사용하여 테이블을 생성하고 데이터를 관리할 수 있습니다.

### MongoDB 연동

-   MongoDB Community Server를 설치하고 환경 변수를 설정합니다.
-   `mongod` 명령어로 서버를 실행하고, `mongo` 셸을 통해 서버에 접속합니다.
-   `use`, `db.createCollection`, `db.collection.insert()` 등의 명령어를 사용하여 데이터베이스와 컬렉션을 관리합니다.

### Spring Boot 연동

-   Spring Initializr를 사용하여 Spring Boot 프로젝트를 생성하고, `web` 의존성을 추가합니다.
-   `@RestController` 어노테이션을 사용하여 RESTful API 엔드포인트를 만듭니다.
-   React 애플리케이션은 이 API를 통해 서버와 데이터를 주고받을 수 있습니다. (CORS 설정 필요)
-   HTML 뷰를 함께 제공하려면 `mustache`와 같은 템플릿 엔진 의존성을 추가할 수 있습니다.