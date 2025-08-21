import { useState } from 'react'
import { Link, Routes, Route, Outlet } from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css"
import './App.css'

// 페이지 컴포넌트 import
import Home from "./pages/home"
import About from "./pages/about"
import Nomatch from "./pages/nomatch"

// 기능별 컴포넌트 import
import Counter from './components/counter'
import ScoreList from './components/score/score_list'
import ScoreWrite from './components/score/score_write'
import BoardList from './components/board/board_list'
import BoardWrite from './components/board/board_write'

function App() {
  // 네비게이션 링크 데이터
  const navigationLinks = [
    { to: "/", label: "Home" },
    { to: "/about", label: "About" },
    { to: "/counter", label: "Counter" },
    { to: "/score/list", label: "성적처리" },
    { to: "/board/list", label: "게시판" }
  ]

  // 라우트 설정 데이터
  const routes = [
    { path: "/", element: <Home /> },
    { path: "/about", element: <About /> },
    { path: "/counter", element: <Counter /> },
    { path: "/score/list", element: <ScoreList /> },
    { path: "/score/insert", element: <ScoreWrite /> },
    { path: "/board/list", element: <BoardList /> },
    { path: "/board/insert", element: <BoardWrite /> },
    { path: "*", element: <Nomatch /> }
  ]

  // 네비게이션 컴포넌트
  const Navigation = () => (
    <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
      <div className="container-fluid">
        <div className="navbar-nav">
          {navigationLinks.map((link, index) => (
            <Link 
              key={index}
              to={link.to} 
              className="nav-link"
            >
              {link.label}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  )

  return (
    <div className='container-fluid'>
      <Navigation />
      
      {/* 라우트 설정 */}
      <Routes>
        {routes.map((route, index) => (
          <Route 
            key={index}
            path={route.path} 
            element={route.element} 
          />
        ))}
      </Routes>
      
      <Outlet />
    </div>
  )
}

export default App
