/*
===============================================================================
                           JavaScript 통합 실습 파일
===============================================================================
이 파일은 JavaScript의 핵심 개념들을 학습 순서에 맞게 통합한 실습 파일입니다.

학습 순서:
1. 변수와 기본 개념
2. 함수 기본
3. 반복문
4. 함수 심화 (배열 메소드)
5. 객체와 JSON
6. 클래스
7. 콜백과 동기/비동기
8. Promise와 async/await
9. 예외처리
===============================================================================
*/

console.log("=".repeat(80));
console.log("            JavaScript 통합 실습 시작");
console.log("=".repeat(80));

/*
===============================================================================
1. 변수와 기본 개념 (var vs let)
===============================================================================
*/
console.log("\n📚 1. 변수와 기본 개념 (var vs let)");
console.log("-".repeat(50));

/*
var - 자바스크립트가 인터프리터 언어라서 굳이 변수 선언을 하지 않아도 된다. 
변수선언을 하려면 var을 사용했었음  
*/

console.log("1-1. var의 특징 (호이스팅):");
a = 10;
var a; // 나중에 변수 선언을 한다.
console.log("a =", a);

// 호이스팅 - 블럭안에 새로운 변수가 생성되었어야 하는데 안되고 있음 그래서 let가 나옴
msg = "hello";
if (true) { // 무조건 if문 안에 들어가길 원함 
    var msg = "안녕하세요";
}
console.log("msg (var 사용시) =", msg); // "안녕하세요"가 출력됨

console.log("\n1-2. 증감 연산자:");
// i=i+1, i+=1, i++, ++i 
// ++i, i++  : 독자적으로 쓰면 차이가 없다. 
// 다른연산자와 함께 쓸 경우에 문제 있음 
let x = 5;
let y = ++x;   // =, ++ 연산우선순위 - 전치연산자는 무엇보다 연산우선순위가 높다. 
               // ++x;  x=6    y=x    
console.log(`x=${x} y=${y}`); // 둘다 6이 나옴 

x = 5;
y = x++;   // y=x  x++      y=5  x=6
console.log(`x=${x} y=${y}`);

/*
===============================================================================
2. 함수 기본
===============================================================================
*/
console.log("\n📚 2. 함수 기본");
console.log("-".repeat(50));

console.log("2-1. 기본 함수 선언:");
function add(x, y) {
    return x + y;
}

// 1~N까지 더해서 출력하는 함수 
function sigma(limit = 10) {
    let s = 0;
    for (let i = 1; i <= limit; i++) {
        s += i;
    }
    return s;
}

console.log("add(4,5) =", add(4, 5));
console.log("sigma(10) =", sigma(10));

console.log("\n2-2. 함수 표현식과 화살표 함수:");
/*
함수  - 미리 만들고 메모리 계속 차지하고 있음
함수표현식 - 일시적인 쓰고 버리는 함수, 함수이름이 없다. 
화살표함수(람다), this사용불가 (python에서 self와 같은 역할)
*/

let add2 = function (x, y) {
    return x + y;
}

let add3 = (x, y) => x + y;

console.log("add2(10,20) =", add2(10, 20));
console.log("add3(10,20) =", add3(10, 20));

/*
===============================================================================
3. 반복문
===============================================================================
*/
console.log("\n📚 3. 반복문");
console.log("-".repeat(50));

console.log("3-1. 기본 for문:");
console.log("1~5까지 출력하기");
for (let i = 1; i <= 5; i++) {
    console.log(`i=${i}`);
}

console.log("\n3-2. 배열과 반복문:");
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("배열:", arr);

console.log("\n일반 for문:");
for (let i = 0; i < arr.length && i < 5; i++) {
    console.log(`arr[${i}] = ${arr[i]}`);
}

console.log("\nfor...in (인덱스):");
let count = 0;
for (let i in arr) {
    console.log(`i=${i} arr[i]=${arr[i]}`);
    if (++count >= 5) break;
}

console.log("\nfor...of (값):");
count = 0;
for (let value of arr) {
    console.log(`value=${value}`);
    if (++count >= 5) break;
}

console.log("\n3-3. 객체 배열 순회:");
let persons = [
    { name: "홍길동", phone: "010-0000-0001" },
    { name: "임꺽정", phone: "010-0000-0002" },
    { name: "장길산", phone: "010-0000-0003" }
];

console.log("\nforEach 사용:");
persons.forEach((p, index) => {
    console.log(`${index + 1}. ${p.name} ${p.phone}`);
});

/*
===============================================================================
4. 함수 심화 (배열 메소드)
===============================================================================
*/
console.log("\n📚 4. 함수 심화 (배열 메소드)");
console.log("-".repeat(50));

console.log("4-1. filter 메소드:");
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 짝수 찾기
let evenNumbers = numbers.filter(n => n % 2 == 0);
console.log("짝수:", evenNumbers);

// 3의 배수 찾기
let multiplesOf3 = numbers.filter(n => n % 3 == 0);
console.log("3의 배수:", multiplesOf3);

let words = ["rain", "umbrella", "desk", "note", "assembly",
    "survey", "flower", "cloud", "hospital", "hammer"];

// 'a'가 포함된 단어
let wordsWithA = words.filter(w => w.includes("a"));
console.log("'a'가 포함된 단어:", wordsWithA);

// 특정 사람 찾기
let foundPerson = persons.filter(p => p.name == "임꺽정");
console.log("임꺽정 정보:", foundPerson);

console.log("\n4-2. map 메소드:");
let doubled = numbers.slice(0, 5).map(x => x * 2);
console.log("2배 배열:", doubled);

let upperWords = words.slice(0, 5).map(w => w.toUpperCase());
console.log("대문자 변환:", upperWords);

console.log("\n4-3. find 메소드:");
let firstEven = numbers.find(x => x % 2 == 0);
console.log("첫 번째 짝수:", firstEven);

console.log("\n4-4. reduce 메소드:");
let sum = numbers.reduce((pre, current) => pre + current, 0);
console.log("배열 합계:", sum);

console.log("\n4-5. sort 메소드:");
let sortArr = [11, 2, 13, 4, 5];
console.log("정렬 전:", sortArr);

let ascending = [...sortArr].sort((a, b) => a - b);
console.log("오름차순:", ascending);

let descending = [...sortArr].sort((a, b) => b - a);
console.log("내림차순:", descending);

// 객체 배열 정렬
let items = [
    { name: "Edward", value: 21 },
    { name: "Sharpe", value: 37 },
    { name: "And", value: 45 }
];

let sortedByValue = [...items].sort((x1, x2) => x1.value - x2.value);
console.log("value로 정렬:", sortedByValue);

/*
===============================================================================
5. 객체와 JSON
===============================================================================
*/
console.log("\n📚 5. 객체와 JSON");
console.log("-".repeat(50));

console.log("5-1. 객체 리터럴:");
let user = { "student-name": "홍길동", kor: 90, eng: 80, mat: 80 };
// 키값에 "" or ''를 사용하거나 또는 없어도 된다. 
// student-name  키값안에 특수문자 들어가면 반드시 "" 로 감싸줘야 한다 
console.log("국어점수:", user.kor, "이름:", user["student-name"]);

// 새로운 필드 추가하기 
user["total"] = user.kor + user.eng + user.mat;
user["avg"] = user.total / 3;
console.log("사용자 정보:", user);

console.log("\n5-2. 객체 배열과 메소드:");
let students = [
    { name: "A", kor: 90, eng: 80, mat: 90 },
    { name: "B", kor: 70, eng: 80, mat: 70 },
    { name: "C", kor: 80, eng: 80, mat: 60 }
];

students.forEach(s => {
    s.total = s.kor + s.eng + s.mat;
    s.avg = s.total / 3;
});

console.log("학생 정보:");
students.forEach(s => console.log(`${s.name}: 총점 ${s.total}, 평균 ${s.avg.toFixed(1)}`));

// 총점으로 내림차순 정렬
let sortedStudents = [...students].sort((a, b) => b.total - a.total);
console.log("\n총점 순위:");
sortedStudents.forEach((s, i) => console.log(`${i + 1}위: ${s.name} (${s.total}점)`));

console.log("\n5-3. 객체 메소드와 this:");
let person = {
    name: "홍길동",
    age: 23,
    // 키에 값만 저장이 아니라 함수도 저장할 수 있다 
    display: function () {
        console.log(`${this.name} ${this.age}`);
        // this - 객체 자신 
        // this생략불가 
    },
    setValue: function (name, age) {
        this.name = name;
        this.age = age;
    }
};
// 화살표함수는 this를 접근할 수 없다. 그래서 람다는 불가능, 함수표현식만 가능하다

person.setValue("임꺽정", 33);
person.display();

/*
객체리터럴과 json 
객체리터럴은 객체를 만들고 생성자, 지금처럼 함수도 저장가능하다 
json 은 함수나 생성자 없고, 네트워크를 이용해 정보를 주고받을때 사용한다 
데이터 전송용, 데이터만 
*/

/*
===============================================================================
6. 클래스
===============================================================================
*/
console.log("\n📚 6. 클래스");
console.log("-".repeat(50));

class Person {
    // 생성자 
    constructor(name = "", age = 0) {
        this.name = name;
        this.age = age;
    }

    display() {
        console.log(this.name, this.age);
    }
}

let personInstance = new Person("홍길동", 33);
personInstance.display();

/*
===============================================================================
7. 콜백과 동기/비동기
===============================================================================
*/
console.log("\n📚 7. 콜백과 동기/비동기");
console.log("-".repeat(50));

console.log("7-1. 콜백 함수:");
function myfunc(callback, x, y) {
    let result = callback(x, y);
    console.log(`${x} ${y} = ${result}`);
}

function addFunc(x, y) {
    return x + y;
}

myfunc(addFunc, 8, 7);
myfunc((x, y) => x - y, 8, 7);
myfunc((x, y) => x * y, 8, 7);

console.log("\n7-2. 동기식 처리:");
function heavyTask() {
    console.log("무거운 작업 시작...");
    let s = 0;
    for (let i = 1; i <= 1000000; i++) {
        s += i;
    }
    console.log("무거운 작업 완료, 결과:", s);
}

function lightTask() {
    for (let i = 1; i <= 5; i++) {
        console.log("가벼운 작업:", i);
    }
}

console.log("동기식 실행:");
heavyTask();
lightTask();

console.log("\n7-3. 비동기식 처리 시뮬레이션:");
console.log("비동기식 실행 시뮬레이션:");

// setTimeout을 사용하여 비동기 처리 시뮬레이션
setTimeout(() => {
    console.log("비동기 무거운 작업 완료!");
}, 100);

console.log("비동기 가벼운 작업 즉시 실행");

/*
Node.js 환경에서만 작동하는 파일 시스템 코드는 주석 처리
let fs = require('fs');

// 동기식 파일 읽기
try {
    let data = fs.readFileSync('./myscript.js', 'utf-8');
    console.log("동기식 파일 내용:", data);
} catch (e) {
    console.log("파일 읽기 오류:", e);
}

// 비동기식 파일 읽기
fs.readFile('./myscript.js', 'utf-8', function(error, data) {
    if (error) {
        console.log("파일 읽기 오류:", error);
    } else {
        console.log("비동기식 파일 내용:", data);
    }
});
*/

/*
===============================================================================
8. Promise와 async/await
===============================================================================
*/
console.log("\n📚 8. Promise와 async/await");
console.log("-".repeat(50));

console.log("8-1. Promise 기본:");
let promise = new Promise(function (resolve, reject) {
    let sum = 0;
    for (let i = 1; i <= 10; i++) {
        sum += i;
    }
    resolve(sum); // return 사용불가 
    // reject("fail");
});

// 동기식 함수를 => 비동기식으로 바꿔주는 클래스임 
promise
    .then((response) => {
        console.log("Promise 결과:", response);
        response = response * 100;
        return response;
    })
    .then((response) => {
        console.log("Promise 체인:", response);
    })
    .catch(e => {
        console.log("Promise 오류:", e);
    })
    .finally(() => {
        console.log("Promise 완료");
    });

console.log("Promise 객체:", promise);

console.log("\n8-2. async/await:");
// 일반함수앞에 async 를 붙이면 비동기객체로 전환시켜라
async function sigmaAsync(limit = 10) {
    let s = 0;
    for (let i = 1; i <= limit; i++) {
        s += i;
    }
    return s;
}

console.log("async 함수 직접 호출:", sigmaAsync(100));

sigmaAsync(1000)
    .then((r) => {
        console.log("async 결과:", r);
    });

// await 사용 예제
async function main() {
    let result = await sigmaAsync(100);
    console.log("await 결과:", result);
    console.log("await 처리 완료");
}

main();

/*
===============================================================================
9. 예외처리
===============================================================================
*/
console.log("\n📚 9. 예외처리");
console.log("-".repeat(50));

console.log("9-1. JSON 파싱 예외처리:");
// let jsondata = "{bad json}";
// 객체리터럴은 '' "" 없거나 다 되는데  json은 키값에 반드시 "" 만 된다.
let jsondata = '{"name":"홍길동","age":23}';

try {
    // 데이터 송수신할때 실제로는 json객체를 주고 받는게 아니고 json 형태의 
    // 문자열을 주고 받는다. 그래서 파싱작업을 해야 한다. 
    // JSON.parse <=> JSON.stringify 
    let userFromJson = JSON.parse(jsondata);
    console.log("JSON 파싱 성공:", userFromJson.name, userFromJson.age);
} catch (e) {
    console.log("JSON 파싱 에러:", e);
}

console.log("\n9-2. 잘못된 JSON 처리:");
let badJsondata = '{bad json}';
try {
    let userFromBadJson = JSON.parse(badJsondata);
    console.log("파싱 성공:", userFromBadJson.name);
} catch (e) {
    console.log("JSON 파싱 실패 - 올바른 예외 처리");
}

/*
===============================================================================
                           실습 완료
===============================================================================
*/
console.log("\n" + "=".repeat(80));
console.log("            JavaScript 통합 실습 완료!");
console.log("=".repeat(80));

console.log("\n🎯 학습한 내용:");
console.log("✅ 1. 변수와 기본 개념 (var vs let, 호이스팅)");
console.log("✅ 2. 함수 기본 (선언, 표현식, 화살표 함수)");
console.log("✅ 3. 반복문 (for, for...in, for...of, forEach)");
console.log("✅ 4. 함수 심화 (filter, map, find, reduce, sort)");
console.log("✅ 5. 객체와 JSON (리터럴, 메소드, this)");
console.log("✅ 6. 클래스 (ES6 클래스, 생성자, 메소드)");
console.log("✅ 7. 콜백과 동기/비동기 (콜백 함수, 실행 순서)");
console.log("✅ 8. Promise와 async/await (비동기 처리)");
console.log("✅ 9. 예외처리 (try-catch, JSON 파싱)");

console.log("\n💡 다음 단계:");
console.log("- DOM 조작과 이벤트 처리");
console.log("- AJAX와 Fetch API");
console.log("- 모듈 시스템 (import/export)");
console.log("- ES6+ 고급 기능들"); 