# HTML 기초 정리

## 목차

1. [HTML 개요](#1-html-개요)
2. [웹 시스템의 기본 구조](#2-웹-시스템의-기본-구조)
3. [form 태그와 정보 전달](#3-form-태그와-정보-전달)
4. [HTML 기본 구조](#4-html-기본-구조)
5. [HTML 주요 태그](#5-html-주요-태그)
6. [시맨틱 태그](#시맨틱-태그)
7. [HTML 문서 예시](#html-문서-예시)
8. [참고 자료](#참고-자료)

---

## 1. HTML 개요

- **HTML**(HyperText Markup Language): 웹 문서의 구조를 정의하는 마크업 언어
- **HTML5**: 최신 표준, 다양한 멀티미디어 지원, 시맨틱 태그 도입
- **하이퍼텍스트**: 문서 내에서 다른 문서나 위치로 이동할 수 있는 링크 제공
- **링크 예시**: `<a href="#section">이동</a>`
- **색상 표현**
    - RGB: `rgb(255,0,0)` (빨강)
    - HEX: `#ff0000` (빨강)
    - 1byte(0~255)씩 R, G, B, (A: 투명도)

---

## 2. 웹 시스템의 기본 구조

- **서버**: 서비스를 제공하는 컴퓨터(하드웨어/소프트웨어)
- **클라이언트**: 서비스를 요청하는 컴퓨터(브라우저 등)
- **웹서버**: 정적 웹페이지(html, css, js, 이미지 등) 제공 (예: Apache, Nginx)
- **WAS(Web Application Server)**: 동적 웹페이지(데이터베이스 연동, 사용자별 맞춤 페이지 등) 제공 (예: Django, Flask, Node.js)
- **정적/동적 웹페이지**
    - 정적: 미리 만들어진 파일 그대로 제공
    - 동적: 요청에 따라 서버에서 새로 생성
- **웹 클라이언트**: 브라우저(Chrome, Edge, Firefox 등)

---

## 3. form 태그와 정보 전달

- **form 태그**: 사용자 입력값을 서버로 전달하는 역할
- **기본 구조**
  ```html
  <form action="/submit" method="post">
    ...
  </form>
  ```
- **action**: 데이터를 전송할 서버의 URL
- **method**: 전송 방식 (get, post)

### GET 방식
- URL에 데이터가 노출됨 (예: `?name=kim&age=20`)
- 전송 데이터 용량 제한(2048byte 내외)
- 보안에 취약, 단순 조회/검색에 적합
- 예시: `http://example.com/search?query=python`

### POST 방식
- 데이터가 HTTP body에 담겨 전송됨
- 대용량 데이터, 파일 첨부 가능
- 보안이 상대적으로 우수(그래도 암호화 필요)
- 예시: 로그인, 회원가입, 파일 업로드 등

---

## 4. input 태그와 다양한 입력 방식

- **input type="text"**: 한 줄 텍스트 입력
- **input type="password"**: 비밀번호 입력(입력값 숨김)
- **input type="radio"**: 여러 옵션 중 하나만 선택
- **input type="checkbox"**: 여러 옵션 중 복수 선택 가능
- **input type="reset"**: 폼 입력값 초기화
- **input type="submit"**: 폼 데이터 서버로 전송
- **input type="button"**: 클릭 이벤트만 발생(자바스크립트와 연동)
- **textarea**: 여러 줄 텍스트 입력
- **select**: 드롭다운 리스트
- **button**: 다양한 용도(기본 submit, type 지정 가능)

### 예시
```html
<form action="/login" method="post">
  <input type="text" name="userid" value="littleconan">
  <input type="password" name="password" value="1234">
  <input type="submit" value="로그인">
</form>
```

---

## 5. name, id, class, value, hidden 속성

- **name**: 서버로 전송되는 데이터의 key(필수)
- **id**: 자바스크립트/스타일에서 요소 식별용(고유)
- **class**: 여러 요소에 공통 스타일/동작 적용
- **value**: 입력값, 서버로 전송되는 실제 데이터
- **hidden**: 사용자에게 보이지 않지만 서버로 값 전송

### 예시
```html
<input type="hidden" name="token" value="abc123">
```

---

## 6. 정보 전달과 HTML의 한계

- HTML 자체는 정보를 저장하지 못함(상태 유지 불가)
- 페이지 이동 시 get/post로만 정보 전달, 이후 정보는 사라짐
- 여러 페이지에서 정보를 유지하려면 서버 세션, 쿠키, 로컬스토리지 등 활용 필요
- 중요한 정보, 파일 등은 반드시 post 방식 사용 권장

---

## 7. 실무 팁

- form 태그는 한 페이지에 하나만 두는 것이 일반적(중첩 불가)
- input의 name 속성은 반드시 지정(서버에서 데이터 수신 가능)
- GET 방식은 검색, 조회 등 노출되어도 무방한 데이터에만 사용
- POST 방식은 로그인, 회원가입, 파일 업로드 등 민감한 데이터에 사용
- input, button, select 등은 label 태그와 함께 사용하면 접근성 향상

---

## 8. 참고 예시

```html
<form action="/register" method="post">
  <label for="username">아이디</label>
  <input type="text" id="username" name="username">
  <label for="pw">비밀번호</label>
  <input type="password" id="pw" name="password">
  <input type="submit" value="회원가입">
</form>
``` 