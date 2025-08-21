# MongoDB 상세 요약

## 1. MongoDB란?

MongoDB는 **문서(Document) 지향적인 NoSQL 데이터베이스**입니다. 관계형 데이터베이스(RDBMS)가 정해진 스키마와 테이블에 데이터를 저장하는 것과 달리, MongoDB는 JSON과 유사한 형태의 유연한 문서에 데이터를 저장합니다. 이로 인해 스키마 변경이 자유롭고, 비정형 데이터를 쉽게 처리할 수 있습니다.

## 2. MongoDB의 주요 특징

-   **유연한 스키마 (Flexible Schema)**: 각 문서가 서로 다른 필드를 가질 수 있어, 변화하는 요구사항에 빠르게 대응할 수 있습니다.
-   **확장성 (Scalability)**: 샤딩(Sharding)을 통해 데이터를 여러 서버에 분산 저장하여 수평적으로 확장하기 용이합니다.
-   **고성능**: 읽기 및 쓰기 작업에 대한 고성능을 제공하며, 특히 대규모 비정형 데이터 처리에 최적화되어 있습니다.
-   **풍부한 쿼리 언어**: 강력한 쿼리 언어를 지원하여 다양한 조건으로 데이터를 쉽게 조회할 수 있습니다.

## 3. 데이터 형태와 구조

MongoDB는 **`Database` > `Collection` > `Document`** 의 계층 구조를 가집니다.

#### ① 문서 (Document)
- **핵심 데이터 단위**로, BSON(Binary JSON) 형식입니다.
- **Key-Value 쌍**으로 이루어져 있으며, 값으로는 문자열, 숫자, 배열, 또는 다른 문서를 포함할 수 있습니다.
- **예시**:
  ```json
  {
    "_id": ObjectId("63f4a9b2c8a7b3e4d5f6g7h8"),
    "username": "user01",
    "age": 30,
    "skills": ["Python", "MongoDB", "Docker"],
    "address": { "city": "서울", "zipcode": "12345" }
  }
  ```

#### ② 컬렉션 (Collection)
- 문서(Document)들의 **그룹**이며, RDBMS의 **테이블(Table)**에 해당하지만 스키마를 강제하지 않습니다.

#### ③ 데이터베이스 (Database)
- 컬렉션(Collection)들을 담는 **최상위 컨테이너**입니다.

## 4. 기본 사용법 (CRUD 명령어)

`users` 컬렉션을 기준으로 한 기본 데이터 조작 명령어입니다.

#### ① 생성 (Create)
- **`insertOne()`**: 하나의 문서를 추가합니다.
  ```javascript
  db.users.insertOne({ "username": "user02", "age": 25 })
  ```
- **`insertMany()`**: 여러 문서를 동시에 추가합니다.
  ```javascript
  db.users.insertMany([
    { "username": "user03", "age": 28 },
    { "username": "user04", "age": 35 }
  ])
  ```

#### ② 조회 (Read)
- **`find()`**: 조건에 맞는 모든 문서를 조회합니다. (조건이 없으면 전체 조회)
  ```javascript
  db.users.find({ age: { $gte: 30 } }) // 30세 이상 사용자 조회
  ```
- **`findOne()`**: 조건에 맞는 첫 번째 문서 하나만 조회합니다.
  ```javascript
  db.users.findOne({ username: "user01" })
  ```

#### ③ 수정 (Update)
- **`updateOne()`**: 조건에 맞는 첫 번째 문서를 수정합니다. (`$set` 사용 권장)
  ```javascript
  db.users.updateOne(
    { username: "user02" },
    { $set: { age: 26 } }
  )
  ```
- **`updateMany()`**: 조건에 맞는 모든 문서를 수정합니다.
  ```javascript
  db.users.updateMany(
    { age: { $lt: 30 } },
    { $set: { status: "active" } }
  )
  ```

#### ④ 삭제 (Delete)
- **`deleteOne()`**: 조건에 맞는 첫 번째 문서를 삭제합니다.
  ```javascript
  db.users.deleteOne({ username: "user04" })
  ```
- **`deleteMany()`**: 조건에 맞는 모든 문서를 삭제합니다.
  ```javascript
  db.users.deleteMany({ age: { $gte: 35 } })
  ```

## 5. 데이터 조회 심화

-   **비교 연산자**: `$gt` (초과), `$gte` (이상), `$lt` (미만), `$lte` (이하), `$in` (배열 내 포함) 등을 사용하여 복잡한 조건을 만들 수 있습니다.
-   **논리 연산자**: `$and`, `$or`, `$not`을 사용하여 여러 조건을 조합할 수 있습니다.
-   **정규표현식**: 필드 값에 대한 패턴 매칭이 가능합니다. (`db.users.find({ username: /^user/ })`)
-   **배열 및 내장 문서 조회**: 점 표기법(`'address.city'`)을 사용하여 내장 문서의 필드에 접근할 수 있습니다.

## 6. 고급 기능 및 도구

-   **GUI 도구**: **MongoDB Compass**를 사용하면 데이터를 시각적으로 관리할 수 있습니다.
-   **조회 결과 필드 제어**: `find()`의 두 번째 인자로 `{ field: 1 }` (포함) 또는 `{ field: 0 }` (제외)을 전달하여 결과 필드를 선택할 수 있습니다.
-   **Auto Sequence (일련번호)**: RDBMS의 `AUTO_INCREMENT` 기능이 없으므로, 별도의 카운터 컬렉션을 만들어 `findAndModify` 명령어로 구현합니다.
-   **사용자 계정**: `admin` 데이터베이스에서 `db.createUser()`를 사용하여 사용자 계정과 권한을 관리합니다.
