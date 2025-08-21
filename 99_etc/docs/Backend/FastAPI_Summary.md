# FastAPI 상세 요약

## 1. FastAPI란?

FastAPI는 현대적이고 빠르며(고성능), 파이썬 표준 타입 힌트에 기반하여 API를 구축하기 위한 웹 프레임워크입니다. 2018년에 처음 등장했으며, **Starlette**(웹 부분)과 **Pydantic**(데이터 유효성 검사 부분)이라는 두 핵심 라이브러리를 기반으로 만들어졌습니다.

RESTful API 개발에 최적화되어 있으며, 뛰어난 생산성과 성능을 제공하여 인공지능 모델 서빙이나 마이크로서비스 아키텍처에 특히 유용합니다.

## 2. FastAPI의 기반 기술과 작동 방식

-   **Starlette**: 고성능 ASGI(Asynchronous Server Gateway Interface) 프레임워크로, FastAPI의 웹 라우팅, 비동기 처리 등 핵심적인 웹 기능을 담당합니다.
-   **Pydantic**: 파이썬 타입 힌트를 사용하여 데이터 유효성 검사, 직렬화, 자동 문서 생성을 지원합니다. 개발자가 데이터 모델을 클래스로 정의하면, Pydantic이 알아서 데이터를 검증하고 변환해줍니다.
-   **ASGI (Asynchronous Server Gateway Interface)**: FastAPI는 `uvicorn`과 같은 ASGI 서버 위에서 동작합니다. ASGI는 파이썬의 비동기 기능을 활용하여 다수의 요청을 동시에 효율적으로 처리할 수 있게 해주는 표준 인터페이스입니다. 이 덕분에 FastAPI는 Node.js나 Go에 버금가는 높은 성능을 낼 수 있습니다.

## 3. FastAPI의 주요 특징

-   **높은 성능**: 비동기 처리를 효율적으로 지원하여 대규모 요청을 빠르게 처리할 수 있습니다.
-   **빠른 개발 속도**: 타입 힌트를 활용하여 코드 자동 완성 및 오류 검사를 강화하고, 코드 중복을 최소화하여 생산성을 높입니다.
-   **자동 API 문서 생성**: OpenAPI(Swagger UI)와 ReDoc 표준을 기반으로 API 문서를 자동으로 생성합니다. `# FastAPI 상세 요약

## 1. FastAPI란?

FastAPI는 현대적이고 빠르며(고성능), 파이썬 표준 타입 힌트에 기반하여 API를 구축하기 위한 웹 프레임워크입니다. 2018년에 처음 등장했으며, **Starlette**(웹 부분)과 **Pydantic**(데이터 유효성 검사 부분)이라는 두 핵심 라이브러리를 기반으로 만들어졌습니다.

RESTful API 개발에 최적화되어 있으며, 뛰어난 생산성과 성능을 제공하여 인공지능 모델 서빙이나 마이크로서비스 아키텍처에 특히 유용합니다.

## 2. FastAPI의 기반 기술과 작동 방식

-   **Starlette**: 고성능 ASGI(Asynchronous Server Gateway Interface) 프레임워크로, FastAPI의 웹 라우팅, 비동기 처리 등 핵심적인 웹 기능을 담당합니다.
-   **Pydantic**: 파이썬 타입 힌트를 사용하여 데이터 유효성 검사, 직렬화, 자동 문서 생성을 지원합니다.
-   **ASGI (Asynchronous Server Gateway Interface)**: FastAPI는 `uvicorn`과 같은 ASGI 서버 위에서 동작하며, 파이썬의 비동기 기능을 활용하여 다수의 요청을 동시에 효율적으로 처리합니다.

## 3. FastAPI의 주요 특징

-   **높은 성능**: 비동기 처리를 효율적으로 지원하여 대규모 요청을 빠르게 처리할 수 있습니다.
-   **빠른 개발 속도**: 타입 힌트를 활용하여 코드 자동 완성 및 오류 검사를 강화하고, 생산성을 높입니다.
-   **자동 API 문서 생성**: OpenAPI(Swagger UI)와 ReDoc 표준을 기반으로 API 문서를 자동으로 생성합니다. (`/docs`, `/redoc`)
-   **강력한 데이터 유효성 검사**: Pydantic을 통해 요청 및 응답 데이터의 유효성을 자동으로 검사합니다.
-   **직관적인 사용법**: 파이썬 표준 타입 힌트를 그대로 사용하므로 코드가 명확하고 가독성이 좋습니다.

## 4. 설치 및 실행

1.  **설치**:
    ```bash
    pip install fastapi uvicorn
    ```
2.  **실행** (`main.py` 파일이 있다고 가정):
    ```bash
    uvicorn main:app --reload
    ```

## 5. 핵심 사용법 및 코드 예시

아래 예시들은 `main.py`라는 파일에 작성된 것으로 가정합니다.

### ① 기본 API 생성

가장 간단한 FastAPI 애플리케이션입니다.

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

### ② 경로 매개변수 (Path Parameter)

URL 경로의 일부를 변수로 사용하여 특정 리소스를 식별합니다.

-   **요청 URL**: `/items/10`
-   **설명**: `item_id`의 타입으로 `int`를 지정하면, FastAPI는 자동으로 데이터 타입을 검증하고 변환합니다. 만약 숫자가 아닌 값이 들어오면 에러를 반환합니다.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": f"Item ID는 {item_id}입니다."}
```

### ③ 쿼리 매개변수 (Query Parameter)

URL의 `?` 뒤에 key=value 형태로 데이터를 전달하여 필터링, 정렬 등에 사용합니다.

-   **요청 URL**: `/users?skip=0&limit=10`
-   **설명**: 함수 매개변수 중 경로 매개변수가 아닌 것들은 자동으로 쿼리 매개변수로 인식됩니다. 기본값을 설정하면 선택적(optional) 매개변수가 됩니다.

```python
from typing import Union

@app.get("/users")
def read_users(skip: int = 0, limit: int = 10, q: Union[str, None] = None):
    result = {"skip": skip, "limit": limit}
    if q:
        result.update({"q": q})
    return result
```

### ④ 요청 본문 (Request Body) - Pydantic 모델 사용

`POST`, `PUT` 요청 시 복잡한 데이터를 JSON 형태로 전송합니다. Pydantic 모델을 사용하여 데이터 구조를 정의하고 유효성을 검사하는 것이 가장 일반적입니다.

-   **요청**: `POST /items/`
-   **Request Body (JSON)**:
    ```json
    {
        "name": "My Item",
        "price": 15.5,
        "is_offer": true
    }
    ```
-   **설명**: `Item` 모델을 정의하면, FastAPI는 요청 본문을 파싱하여 `Item` 객체로 변환하고, 데이터 타입과 구조가 올바른지 자동으로 검증합니다.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}
```

## 6. 주요 사용 사례

-   **고성능 REST API 서버**: 대규모 트래픽을 처리해야 하는 서비스의 백엔드 API 서버 구축
-   **머신러닝 모델 서빙**: 학습된 AI 모델을 API로 배포하여 외부 서비스에서 쉽게 활용
-   **마이크로서비스 아키텍처**: 작고 독립적인 서비스들의 API 서버로 활용
-   **실시간 웹 애플리케이션**: WebSocket을 지원하여 채팅, 실시간 알림 등 구현
`에서 API를 직접 테스트해볼 수 있습니다.
-   **강력한 데이터 유효성 검사**: Pydantic을 통해 요청 및 응답 데이터의 유효성을 자동으로 검사하고, 형식이 맞지 않으면 상세한 에러를 반환하여 안정성을 높입니다.
-   **직관적인 사용법**: 파이썬 표준 타입 힌트를 그대로 사용하므로 코드가 명확하고 가독성이 좋습니다.

## 4. 주요 사용 사례

-   **고성능 REST API 서버**: 대규모 트래픽을 처리해야 하는 서비스의 백엔드 API 서버 구축
-   **머신러닝 모델 서빙**: 학습된 AI 모델을 API로 배포하여 외부 서비스에서 쉽게 활용할 수 있도록 지원
-   **마이크로서비스 아키텍처**: 작고 독립적인 서비스들을 연결하여 하나의 큰 애플리케이션을 구성할 때 각 서비스의 API 서버로 활용
-   **실시간 웹 애플리케이션**: WebSocket을 지원하여 채팅, 실시간 알림 등과 같은 기능을 구현

## 5. 설치 및 실행

1.  **Conda 가상환경 생성 및 활성화**:
    ```bash
    conda create –n backend
    conda activate backend
    ```
2.  **FastAPI 및 Uvicorn 설치**:
    ```bash
    conda install fastapi
    conda install uvicorn
    ```
3.  **실행**:
    ```bash
    python –m uvicorn [파일명]:app --reload
    ```

## 6. Pydantic 모델을 사용해야 하는 이유

Pydantic 모델은 FastAPI의 핵심 기능과 직결되며, 사용 시 다음과 같은 강력한 이점을 제공합니다.

-   **데이터 유효성 검사**: 요청 데이터의 타입과 필수 필드를 자동으로 검사하여 잘못된 데이터 유입을 사전에 차단합니다.
-   **자동 문서화**: API 문서에 요청 및 응답 데이터의 구조와 타입 정보가 상세하게 표시되어 협업을 용이하게 합니다.
-   **코드 가독성 및 재사용성**: 데이터 구조를 한 곳에서 체계적으로 관리하여 코드가 깔끔해지고 유지보수가 쉬워집니다.
-   **복잡한 데이터 구조 처리**: 중첩된 JSON 객체나 리스트와 같은 복잡한 구조를 직관적으로 정의하고 처리할 수 있습니다.
