# JavaScript와 jQuery 프로그래밍 가이드

## 목차

1. [JavaScript 소개](#javascript-소개)
2. [개발환경 설정](#개발환경-설정)
3. [기본 문법](#기본-문법)
4. [변수와 자료형](#변수와-자료형)
5. [연산자](#연산자)
6. [조건문과 반복문](#조건문과-반복문)
7. [함수](#함수)
8. [객체와 배열](#객체와-배열)
9. [클래스와 상속](#클래스와-상속)
10. [비동기 처리](#비동기-처리)
11. [DOM 조작](#dom-조작)
12. [이벤트 처리](#이벤트-처리)
13. [jQuery 기초](#jquery-기초)
14. [AJAX](#ajax)

---

## JavaScript 소개

### JavaScript란?
- 웹페이지에 생동감을 불어넣기 위해 만들어진 프로그래밍 언어
- 브라우저에서 번역되고 실행되는 스크립트 언어
- 특별한 준비나 컴파일 없이 텍스트 형태로 작성하고 실행 가능
- 처음에는 'LiveScript'라는 이름으로 시작됨

### JavaScript의 발전
- **초기**: 클라이언트 사이드 스크립트 언어
- **현재**: 서버 사이드 개발도 가능 (Node.js)
- **모던 JavaScript**: ES6+ 문법으로 객체지향 개념 강화
- **프레임워크**: React, Vue, Angular 등 다양한 라이브러리 지원

### 브라우저에서 JavaScript가 할 수 있는 일
- 페이지에 새로운 HTML 추가하거나 기존 HTML/스타일 수정
- 마우스 클릭, 포인터 움직임, 키보드 입력 등 사용자 행동에 반응
- 네트워크를 통해 원격 서버에 요청 (AJAX, COMET)
- 쿠키 설정/조회, 사용자에게 메시지 표시
- 클라이언트 측 데이터 저장 (로컬 스토리지)

### 브라우저에서 제한되는 것들
- **파일 시스템 접근**: 디스크 파일 읽기/쓰기 제한
- **디바이스 접근**: 카메라, 마이크 등은 명시적 허가 필요
- **동일 출처 정책**: 다른 도메인의 데이터 접근 제한
- **보안**: 악성 웹페이지로부터 사용자 보호

### JavaScript의 장점
- HTML/CSS와 완전한 통합
- 간단한 일은 간단하게 처리
- 모든 주요 브라우저에서 지원
- 비동기 입출력을 이용한 서버 작성 가능

---

## 개발환경 설정

### 개발 도구 옵션
- **브라우저**: Chrome, Firefox, Safari, Edge (Chrome 권장 - 디버깅 편리)
- **에디터**: Atom, WebStorm, EditPlus, UltraEdit, Visual Studio Code
- **서버**: Ajax 통신을 위해 필요 (Spring Boot, PHP, ASP, Django, Node.js)

### Visual Studio Code 설치
1. https://code.visualstudio.com/Download 에서 다운로드
2. 필수 확장팩 설치:
   - HTML Snippets
   - JavaScript (ES6) code snippets
   - jQuery Code Snippets

### 기본 설정
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript 기본 구조</title>
</head>
<body>
    <script>
        // JavaScript 코드 작성
        console.log("Hello, JavaScript!");
    </script>
</body>
</html>
```

---

## 기본 문법

### 스크립트 작성 방법

#### 1. 내부 스크립트
```html
<script>
    alert('Hello, World!');
</script>
```

#### 2. 외부 스크립트
```html
<script src="js/myscript.js"></script>
```

#### 주의사항
- 스크립트가 길어지면 별도 파일로 분리하는 것이 좋음
- 브라우저 캐시를 통해 성능 향상
- `<script>` 태그는 `src` 속성과 내부 코드를 동시에 가질 수 없음

### 코드 구조

#### 문(Statement)
```javascript
alert('Hello');
alert('World');
```

#### 세미콜론
```javascript
// 세미콜론 사용 (권장)
alert('Hello');
alert('World');

// 줄 바꿈으로 자동 삽입
alert('Hello')
alert('World')
```

#### 주석
```javascript
// 한 줄 주석

/*
여러 줄 주석
*/
```

### 엄격 모드 (Strict Mode)
```javascript
"use strict";

// 엄격 모드에서 실행되는 코드
// 코딩 실수를 잡아내고 안전하지 않은 액션 방지
```

---

## 변수와 자료형

### 변수 선언
```javascript
// 모던 JavaScript
let message = "Hello";
const name = "JavaScript";

// 구버전 (권장하지 않음)
var oldVariable = "old";
```

### 변수명 규칙
- 문자, 숫자, `$`, `_`만 사용 가능
- 첫 글자는 숫자 불가
- 카멜케이스 사용 권장 (camelCase)
- 예약어 사용 불가
- 대소문자 구분

### 자료형

#### 1. 숫자형 (Number)
```javascript
let integer = 42;
let float = 3.14;
let infinity = Infinity;
let notANumber = NaN;

// 특수 값
console.log(1 / 0); // Infinity
console.log("abc" / 2); // NaN
```

#### 2. 문자형 (String)
```javascript
let str1 = "Hello";
let str2 = 'Single quotes';
let str3 = `Template literal: ${str1}`;

// 백틱을 사용한 문자열 보간
let name = "JavaScript";
let message = `Hello, ${name}!`;
```

#### 3. 불린형 (Boolean)
```javascript
let isTrue = true;
let isFalse = false;

// 비교 연산 결과
let isGreater = 4 > 1; // true
```

#### 4. null
```javascript
let age = null; // 값이 없음을 명시적으로 표현
```

#### 5. undefined
```javascript
let x;
console.log(x); // undefined

// 또는 명시적 할당
let y = undefined;
```

#### 6. 객체형 (Object)
```javascript
let user = {
    name: "John",
    age: 30
};
```

#### 7. 심볼형 (Symbol)
```javascript
let id = Symbol("id");
```

### typeof 연산자
```javascript
console.log(typeof 42); // "number"
console.log(typeof "Hello"); // "string"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null); // "object" (언어의 오류)
console.log(typeof {}); // "object"
console.log(typeof function(){}); // "function"
```

### 형변환

#### 문자형 변환
```javascript
let value = String(123); // "123"
let value2 = 123 + ""; // "123"
```

#### 숫자형 변환
```javascript
let num = Number("123"); // 123
let num2 = +"123"; // 123

// 변환 규칙
Number(undefined); // NaN
Number(null); // 0
Number(true); // 1
Number(false); // 0
Number(""); // 0
Number("123abc"); // NaN
```

#### 불린형 변환
```javascript
Boolean(1); // true
Boolean(0); // false
Boolean(""); // false
Boolean("hello"); // true
Boolean(null); // false
Boolean(undefined); // false
```

---

## 연산자

### 산술 연산자
```javascript
let a = 5, b = 2;

console.log(a + b); // 7 (덧셈)
console.log(a - b); // 3 (뺄셈)
console.log(a * b); // 10 (곱셈)
console.log(a / b); // 2.5 (나눗셈)
console.log(a % b); // 1 (나머지)
console.log(a ** b); // 25 (거듭제곱)
```

### 비교 연산자
```javascript
console.log(5 > 3); // true
console.log(5 < 3); // false
console.log(5 >= 5); // true
console.log(5 <= 4); // false

// 동등 연산자 (타입 변환 O)
console.log("2" == 2); // true
console.log(0 == false); // true

// 일치 연산자 (타입 변환 X)
console.log("2" === 2); // false
console.log(0 === false); // false
```

### 논리 연산자
```javascript
let x = true, y = false;

console.log(x && y); // false (AND)
console.log(x || y); // true (OR)
console.log(!x); // false (NOT)
```

### 할당 연산자
```javascript
let x = 5;
x += 3; // x = x + 3 → 8
x -= 2; // x = x - 2 → 6
x *= 2; // x = x * 2 → 12
x /= 3; // x = x / 3 → 4
```

---

## 조건문과 반복문

### if문
```javascript
let age = 18;

if (age >= 18) {
    console.log("성인입니다.");
} else if (age >= 13) {
    console.log("청소년입니다.");
} else {
    console.log("어린이입니다.");
}
```

### 삼항 연산자
```javascript
let age = 20;
let status = age >= 18 ? "성인" : "미성년자";
```

### switch문
```javascript
let day = 3;

switch (day) {
    case 1:
        console.log("월요일");
        break;
    case 2:
        console.log("화요일");
        break;
    case 3:
        console.log("수요일");
        break;
    default:
        console.log("기타");
}
```

### while문
```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
```

### for문
```javascript
// 기본 for문
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// 배열 순회
let flowers = ["작약", "목련", "백일홍", "국화", "장미"];

// for...in (인덱스)
for (let index in flowers) {
    console.log(index, flowers[index]);
}

// for...of (값)
for (let flower of flowers) {
    console.log(flower);
}
```

---

## 함수

### 함수 선언
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

let result = greet("JavaScript");
console.log(result); // Hello, JavaScript!
```

### 함수 표현식
```javascript
let sayHello = function(name) {
    return `Hello, ${name}!`;
};

sayHello("World");
```

### 화살표 함수
```javascript
// 기본 형태
let add = (a, b) => a + b;

// 여러 줄
let multiply = (a, b) => {
    let result = a * b;
    return result;
};

// 매개변수가 하나일 때
let square = x => x * x;

// 매개변수가 없을 때
let sayHello = () => "Hello!";
```

### 매개변수와 기본값
```javascript
function greet(name = "World") {
    return `Hello, ${name}!`;
}

console.log(greet()); // Hello, World!
console.log(greet("JavaScript")); // Hello, JavaScript!
```

### 콜백 함수
```javascript
function processUser(name, callback) {
    console.log(`Processing ${name}...`);
    callback(name);
}

processUser("John", function(name) {
    console.log(`Welcome, ${name}!`);
});

// 화살표 함수로 콜백
processUser("Jane", name => console.log(`Hi, ${name}!`));
```

### 배열 메서드와 화살표 함수
```javascript
let numbers = [1, 2, 3, 4, 5];

// filter - 조건에 맞는 요소만 선택
let evenNumbers = numbers.filter(n => n % 2 === 0);
console.log(evenNumbers); // [2, 4]

// map - 각 요소를 변환
let doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// find - 조건에 맞는 첫 번째 요소
let firstEven = numbers.find(n => n % 2 === 0);
console.log(firstEven); // 2

// reduce - 배열을 하나의 값으로 축소
let sum = numbers.reduce((acc, n) => acc + n, 0);
console.log(sum); // 15
```

---

## 객체와 배열

### 객체 생성과 조작
```javascript
// 객체 생성
let user = {
    name: "John",
    age: 30,
    isAdmin: true
};

// 속성 접근
console.log(user.name); // John
console.log(user["age"]); // 30

// 속성 추가/수정
user.email = "john@example.com";
user.age = 31;

// 속성 삭제
delete user.isAdmin;

// 속성 존재 확인
console.log("name" in user); // true
```

### 객체 메서드
```javascript
let person = {
    name: "Alice",
    age: 25,
    greet: function() {
        return `Hello, I'm ${this.name}`;
    },
    // 단축 문법
    sayAge() {
        return `I'm ${this.age} years old`;
    }
};

console.log(person.greet()); // Hello, I'm Alice
console.log(person.sayAge()); // I'm 25 years old
```

### 배열
```javascript
let fruits = ["apple", "banana", "orange"];

// 배열 조작
fruits.push("grape"); // 끝에 추가
fruits.unshift("strawberry"); // 앞에 추가
fruits.pop(); // 마지막 요소 제거
fruits.shift(); // 첫 번째 요소 제거

// 배열 순회
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```

### 객체 배열
```javascript
let students = [
    { name: "Alice", grade: 85 },
    { name: "Bob", grade: 92 },
    { name: "Charlie", grade: 78 }
];

// 높은 점수 학생 찾기
let topStudent = students.find(student => student.grade > 90);
console.log(topStudent); // { name: "Bob", grade: 92 }

// 평균 계산
let average = students.reduce((sum, student) => sum + student.grade, 0) / students.length;
console.log(average); // 85
```

---

## 클래스와 상속

### 프로토타입 기반 상속
```javascript
// 생성자 함수
function Animal(name) {
    this.name = name;
}

// 프로토타입에 메서드 추가
Animal.prototype.speak = function() {
    return `${this.name} makes a sound`;
};

// 상속
function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function() {
    return `${this.name} barks`;
};

let dog = new Dog("Rex", "Golden Retriever");
console.log(dog.speak()); // Rex barks
```

### ES6 클래스
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        return `${this.name} makes a sound`;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    
    speak() {
        return `${this.name} barks`;
    }
    
    getInfo() {
        return `${this.name} is a ${this.breed}`;
    }
}

let dog = new Dog("Rex", "Golden Retriever");
console.log(dog.speak()); // Rex barks
console.log(dog.getInfo()); // Rex is a Golden Retriever
```

---

## 비동기 처리

### 콜백 지옥 (Callback Hell)
```javascript
// 좋지 않은 예 - 콜백 지옥
getData(function(a) {
    getMoreData(a, function(b) {
        getMoreData(b, function(c) {
            getMoreData(c, function(d) {
                // 계속 중첩...
            });
        });
    });
});
```

### Promise
```javascript
// Promise 생성
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let success = true;
        if (success) {
            resolve("작업 성공!");
        } else {
            reject("작업 실패!");
        }
    }, 1000);
});

// Promise 사용
promise
    .then(result => {
        console.log(result);
        return "다음 작업";
    })
    .then(result => {
        console.log(result);
    })
    .catch(error => {
        console.error(error);
    })
    .finally(() => {
        console.log("항상 실행");
    });
```

### Promise 체인
```javascript
function fetchUser(id) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve({ id: id, name: "User" + id });
        }, 1000);
    });
}

function fetchPosts(userId) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve([
                { id: 1, title: "Post 1", userId: userId },
                { id: 2, title: "Post 2", userId: userId }
            ]);
        }, 1000);
    });
}

fetchUser(1)
    .then(user => {
        console.log("User:", user);
        return fetchPosts(user.id);
    })
    .then(posts => {
        console.log("Posts:", posts);
    });
```

### async/await
```javascript
// Promise를 더 간단하게 사용
async function fetchUserAndPosts(userId) {
    try {
        const user = await fetchUser(userId);
        console.log("User:", user);
        
        const posts = await fetchPosts(user.id);
        console.log("Posts:", posts);
        
        return { user, posts };
    } catch (error) {
        console.error("Error:", error);
    }
}

// 사용
fetchUserAndPosts(1);
```

---

## DOM 조작

### DOM 요소 선택
```javascript
// ID로 선택
let element = document.getElementById('myId');

// 클래스로 선택
let elements = document.getElementsByClassName('myClass');

// 태그로 선택
let divs = document.getElementsByTagName('div');

// CSS 선택자로 선택
let first = document.querySelector('.myClass');
let all = document.querySelectorAll('.myClass');
```

### DOM 조작 예제
```html
<!DOCTYPE html>
<html>
<head>
    <title>DOM 조작 예제</title>
</head>
<body>
    <div id="container">
        <p class="text">원본 텍스트</p>
        <button id="changeBtn">텍스트 변경</button>
    </div>

    <script>
        // 요소 선택
        let textElement = document.querySelector('.text');
        let button = document.getElementById('changeBtn');
        
        // 이벤트 리스너 추가
        button.addEventListener('click', function() {
            textElement.textContent = '변경된 텍스트';
            textElement.style.color = 'blue';
        });
        
        // 새 요소 추가
        let newParagraph = document.createElement('p');
        newParagraph.textContent = '새로운 문단';
        document.getElementById('container').appendChild(newParagraph);
    </script>
</body>
</html>
```

### 테이블 조작
```javascript
// 테이블에 행 추가
function addRow() {
    let table = document.getElementById('myTable');
    let row = table.insertRow();
    
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    
    cell1.textContent = '새 데이터 1';
    cell2.textContent = '새 데이터 2';
}

// 테이블 행 삭제
function deleteRow(rowIndex) {
    let table = document.getElementById('myTable');
    table.deleteRow(rowIndex);
}
```

---

## 이벤트 처리

### 이벤트 리스너
```javascript
// 클릭 이벤트
document.getElementById('myButton').addEventListener('click', function(e) {
    console.log('버튼이 클릭되었습니다!');
    console.log('이벤트 객체:', e);
});

// 키보드 이벤트
document.addEventListener('keydown', function(e) {
    console.log('키가 눌렸습니다:', e.key);
    if (e.key === 'Enter') {
        console.log('엔터키가 눌렸습니다!');
    }
});

// 마우스 이벤트
let element = document.getElementById('myDiv');
element.addEventListener('mouseenter', function() {
    this.style.backgroundColor = 'lightblue';
});
element.addEventListener('mouseleave', function() {
    this.style.backgroundColor = '';
});
```

### 폼 이벤트
```javascript
// 폼 제출 이벤트
document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault(); // 기본 제출 동작 방지
    
    let formData = new FormData(this);
    let name = formData.get('name');
    let email = formData.get('email');
    
    console.log('이름:', name);
    console.log('이메일:', email);
});

// 입력 이벤트
document.getElementById('searchInput').addEventListener('input', function(e) {
    console.log('입력값:', e.target.value);
});
```

### 이벤트 위임
```javascript
// 부모 요소에서 자식 요소의 이벤트 처리
document.getElementById('container').addEventListener('click', function(e) {
    if (e.target.classList.contains('item')) {
        console.log('아이템이 클릭되었습니다:', e.target.textContent);
    }
});
```

---

## jQuery 기초

### jQuery 설치
```html
<!-- CDN 방식 -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!-- 또는 다운로드 방식 -->
<script src="js/jquery.min.js"></script>
```

### jQuery 기본 사용법
```javascript
// 문서 준비 완료 후 실행
$(document).ready(function() {
    // jQuery 코드
});

// 단축 문법
$(function() {
    // jQuery 코드
});
```

### 선택자
```javascript
// 기본 선택자
$("p")              // 모든 p 태그
$("#myId")          // ID가 myId인 요소
$(".myClass")       // 클래스가 myClass인 요소
$("*")              // 모든 요소

// 복합 선택자
$("div p")          // div 안의 모든 p
$("div > p")        // div의 직계 자식 p
$("p:first")        // 첫 번째 p
$("p:last")         // 마지막 p
$("p:even")         // 짝수 번째 p
$("p:odd")          // 홀수 번째 p
```

### 이벤트 처리
```javascript
// 클릭 이벤트
$("#myButton").click(function() {
    alert("버튼이 클릭되었습니다!");
});

// 여러 이벤트
$("#myElement").on({
    mouseenter: function() {
        $(this).css("background-color", "lightblue");
    },
    mouseleave: function() {
        $(this).css("background-color", "");
    },
    click: function() {
        $(this).hide();
    }
});
```

### 내용 조작
```javascript
// 텍스트 읽기/쓰기
let text = $("#myElement").text();
$("#myElement").text("새 텍스트");

// HTML 읽기/쓰기
let html = $("#myElement").html();
$("#myElement").html("<strong>새 HTML</strong>");

// 속성 조작
let value = $("#myInput").val();
$("#myInput").val("새 값");

// 속성 설정
$("#myImage").attr("src", "new-image.jpg");
```

### 애니메이션
```javascript
// 기본 애니메이션
$("#myDiv").hide();
$("#myDiv").show();
$("#myDiv").toggle();

// 페이드 효과
$("#myDiv").fadeIn();
$("#myDiv").fadeOut();
$("#myDiv").fadeToggle();

// 슬라이드 효과
$("#myDiv").slideUp();
$("#myDiv").slideDown();
$("#myDiv").slideToggle();

// 사용자 정의 애니메이션
$("#myDiv").animate({
    left: '250px',
    opacity: '0.5',
    height: '150px',
    width: '150px'
});
```

### 메서드 체이닝
```javascript
$("#myDiv")
    .hide()
    .delay(1000)
    .fadeIn()
    .css("color", "red")
    .addClass("highlight");
```

---

## AJAX

### XMLHttpRequest (순수 JavaScript)
```javascript
// GET 요청
let xhr = new XMLHttpRequest();
xhr.open('GET', 'data.json', true);
xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        let data = JSON.parse(xhr.responseText);
        console.log(data);
    }
};
xhr.send();

// POST 요청
let xhr2 = new XMLHttpRequest();
xhr2.open('POST', 'api/users', true);
xhr2.setRequestHeader('Content-Type', 'application/json');
xhr2.onreadystatechange = function() {
    if (xhr2.readyState === 4 && xhr2.status === 200) {
        console.log('데이터 전송 성공');
    }
};
xhr2.send(JSON.stringify({ name: 'John', age: 30 }));
```

### jQuery AJAX
```javascript
// GET 요청
$.ajax({
    url: 'data.json',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        console.log('성공:', data);
    },
    error: function(xhr, status, error) {
        console.error('오류:', error);
    }
});

// POST 요청
$.ajax({
    url: 'api/users',
    type: 'POST',
    data: JSON.stringify({ name: 'John', age: 30 }),
    contentType: 'application/json',
    success: function(response) {
        console.log('전송 성공:', response);
    }
});

// 간단한 GET 요청
$.get('data.json', function(data) {
    console.log(data);
});

// 간단한 POST 요청
$.post('api/users', { name: 'John', age: 30 }, function(response) {
    console.log(response);
});
```

### Fetch API (모던 JavaScript)
```javascript
// GET 요청
fetch('data.json')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

// POST 요청
fetch('api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: 'John', age: 30 })
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));

// async/await 사용
async function fetchData() {
    try {
        const response = await fetch('data.json');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

### 실제 사용 예제
```javascript
// 사용자 목록 가져오기
function loadUsers() {
    $.ajax({
        url: 'api/users',
        type: 'GET',
        success: function(users) {
            let userList = $('#userList');
            userList.empty();
            
            users.forEach(function(user) {
                userList.append(`
                    <li>
                        <strong>${user.name}</strong> (${user.email})
                        <button onclick="deleteUser(${user.id})">삭제</button>
                    </li>
                `);
            });
        },
        error: function() {
            alert('사용자 목록을 불러올 수 없습니다.');
        }
    });
}

// 사용자 삭제
function deleteUser(userId) {
    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            url: `api/users/${userId}`,
            type: 'DELETE',
            success: function() {
                loadUsers(); // 목록 새로고침
            },
            error: function() {
                alert('삭제 실패');
            }
        });
    }
}
```

---

## 실습 프로젝트

### 간단한 할 일 관리 앱
```html
<!DOCTYPE html>
<html>
<head>
    <title>할 일 관리</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <style>
        .completed { text-decoration: line-through; }
        .todo-item { margin: 10px 0; }
    </style>
</head>
<body>
    <h1>할 일 관리</h1>
    
    <div>
        <input type="text" id="todoInput" placeholder="할 일을 입력하세요">
        <button id="addBtn">추가</button>
    </div>
    
    <ul id="todoList"></ul>

    <script>
        $(document).ready(function() {
            let todos = [];
            
            // 할 일 추가
            $('#addBtn').click(function() {
                let text = $('#todoInput').val().trim();
                if (text) {
                    todos.push({
                        id: Date.now(),
                        text: text,
                        completed: false
                    });
                    $('#todoInput').val('');
                    renderTodos();
                }
            });
            
            // 엔터키로 추가
            $('#todoInput').keypress(function(e) {
                if (e.which === 13) {
                    $('#addBtn').click();
                }
            });
            
            // 할 일 렌더링
            function renderTodos() {
                let list = $('#todoList');
                list.empty();
                
                todos.forEach(function(todo) {
                    let item = $(`
                        <li class="todo-item">
                            <input type="checkbox" ${todo.completed ? 'checked' : ''} 
                                   onchange="toggleTodo(${todo.id})">
                            <span class="${todo.completed ? 'completed' : ''}">${todo.text}</span>
                            <button onclick="deleteTodo(${todo.id})">삭제</button>
                        </li>
                    `);
                    list.append(item);
                });
            }
            
            // 전역 함수로 정의
            window.toggleTodo = function(id) {
                let todo = todos.find(t => t.id === id);
                if (todo) {
                    todo.completed = !todo.completed;
                    renderTodos();
                }
            };
            
            window.deleteTodo = function(id) {
                todos = todos.filter(t => t.id !== id);
                renderTodos();
            };
        });
    </script>
</body>
</html>
```

---

## 마무리

### 학습 정리
이 가이드에서 다룬 내용:
- **JavaScript 기초**: 문법, 변수, 자료형, 연산자
- **제어 구조**: 조건문, 반복문, 함수
- **객체 지향**: 클래스, 상속, 프로토타입
- **비동기 처리**: Promise, async/await
- **DOM 조작**: 요소 선택, 이벤트 처리
- **jQuery**: 선택자, 이벤트, 애니메이션
- **AJAX**: 비동기 통신, 데이터 교환

### 추가 학습 자료
- **모던 JavaScript 튜토리얼**: https://ko.javascript.info/
- **MDN Web Docs**: https://developer.mozilla.org/ko/docs/Web/JavaScript
- **jQuery 공식 문서**: https://jquery.com/
- **ES6+ 문법**: https://github.com/lukehoban/es6features

### 실무 팁
1. **코드 품질**: ESLint, Prettier 등 도구 사용
2. **모듈화**: ES6 모듈 시스템 활용
3. **성능 최적화**: 불필요한 DOM 조작 최소화
4. **크로스 브라우징**: 다양한 브라우저에서 테스트
5. **보안**: XSS, CSRF 등 보안 이슈 고려

### 다음 단계
- React, Vue, Angular 등 프레임워크 학습
- Node.js로 서버 사이드 개발
- TypeScript로 타입 안정성 향상
- 웹팩, 바벨 등 빌드 도구 활용
