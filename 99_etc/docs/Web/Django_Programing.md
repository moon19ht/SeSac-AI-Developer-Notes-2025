# Django 프로그래밍 가이드

## 목차

1. [Django 소개](#django-소개)
2. [개발환경 설정](#개발환경-설정)
3. [Django 프레임워크](#django-프레임워크)
4. [MVT 패턴](#mvt-패턴)
5. [URL과 View](#url과-view)
6. [앱 개발](#앱-개발)
7. [모델과 데이터베이스](#모델과-데이터베이스)
8. [MySQL 연동](#mysql-연동)
9. [MongoDB 연동](#mongodb-연동)
10. [템플릿 시스템](#템플릿-시스템)
11. [폼 처리](#폼-처리)
12. [사용자 인증](#사용자-인증)
13. [Restful API](#restful-api)
14. [배포](#배포)

---

## Django 소개

### Django란?
- 파이썬 기반으로 작성된 오픈소스 웹 애플리케이션 프레임워크
- 프레임워크란 프로그램 개발에 사용되는 기본 개념 구조 (뼈대, 골조)
- 파이썬 기반의 동적 웹 개발을 위한 구조적 도구
- 공식 사이트: https://www.djangoproject.com/

### Django 프레임워크의 특징

#### 1. 빠른 개발 (Fast Development)
- 간단한 규칙만 익히면 빠르게 웹 프로그램 개발 가능
- 예시: "Hello World" 출력
```python
def index(request):
    return HttpResponse("Hello World")
```

#### 2. 보안 (Security)
- SQL 인젝션, XSS, CSRF, 클릭재킹 등 보안 공격에 대한 기본 방어 기능 제공
- 개발자가 보안에 크게 신경 쓰지 않아도 기본적인 보안 유지

#### 3. 다양한 기능 (Rich Features)
- 웹 개발에 필요한 다양한 기능들을 내장으로 제공

### Django를 사용하는 주요 사이트들
- Instagram, Pinterest, Mozilla, Disqus 등 다수의 대형 사이트에서 활용

---

## 개발환경 설정

### 1. 개발 도구 옵션
- **텍스트 에디터**: Edit Plus, Notepad++
- **IDE**: PyCharm, Eclipse + Python Plugin
- **Visual Studio**: Python 개발 도구 (Express 버전 지원)
- **권장**: Visual Studio Code

### 2. Anaconda 설치

#### 설치 과정
1. https://www.anaconda.com/distribution/ 에서 다운로드
2. 64비트 버전 선택 (딥러닝 지원)
3. 설치 시 "Add Anaconda to PATH" 옵션 반드시 체크

#### 환경변수 설정
```
C:\ProgramData\Anaconda3
C:\ProgramData\Anaconda3\Library\mingw-w64\bin
C:\ProgramData\Anaconda3\Library\usr\bin
C:\ProgramData\Anaconda3\Library\bin
C:\ProgramData\Anaconda3\Scripts
```

### 3. Visual Studio Code 설정

#### 기본 설정
- 파일 → 기본설정 → 설정 → Zoom (화면 크기 설정)
- 파일 → 기본설정 → 설정 → Theme → Default Light 설정
- 자동저장 체크

#### 프로젝트 설정
1. 파일 → 폴더 열기 → django_workspace 폴더 생성
2. 디버그 → 구성 추가 → Anaconda 선택
3. Ctrl + Shift + F → 확장 → Anaconda Extension 설치

### 4. 웹서버 종류

#### 개발용 서버
- **runserver**: Django 내장 개발 서버

#### 운영용 서버
- **Apache**: 
  - 스레드/프로세스 기반 구조
  - 요청 하나당 스레드 하나 처리
  - 사용자 증가 시 메모리 및 CPU 낭비 발생

- **Nginx**:
  - 비동기 Event-Driven 기반 구조
  - 다수의 연결을 효과적으로 처리
  - Apache보다 적은 리소스로 빠른 동작

---

## Django 프레임워크

### 1. 가상환경 (Virtual Environment)

#### 가상환경의 필요성
- 프로젝트별로 독립적인 환경 구성
- 각 프로젝트마다 다른 Python 및 라이브러리 버전 사용 가능
- 의존성 충돌 방지

#### 가상환경 생성 방법

**방법 1: Python venv 사용**
```bash
cd \
mkdir virtual
cd virtual
python -m venv mysite
cd mysite/Scripts
activate          # 가상환경 활성화
deactivate        # 가상환경 비활성화
```

**방법 2: Anaconda 사용**
```bash
conda create --name mysite
conda activate mysite
```

### 2. Django 라이브러리 설치

```bash
conda activate mysite
pip install django
# 또는 버전 지정
pip install Django~=2.0.0
```

#### 버전 확인
```bash
python -m django --version
```

### 3. Django 프로젝트 생성

```bash
cd \
mkdir django_workspace
cd django_workspace
mkdir mysite
cd mysite
django-admin startproject config .
```

### 4. 서버 구동
```bash
python manage.py runserver
```

---

## MVT 패턴

Django는 MVT(Model-View-Template) 패턴을 사용합니다.

- **Model**: 데이터베이스와 상호작용하는 부분
- **View**: 비즈니스 로직을 처리하는 부분
- **Template**: 사용자에게 보여지는 화면 부분

---

## URL과 View

### 1. 앱 생성
```bash
django-admin startapp blog
```

### 2. View 함수 작성
```python
# blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

### 3. URL 연결

#### 메인 urls.py 설정
```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

#### 앱별 urls.py 설정
```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 4. POST 방식 처리

#### CSRF 보안 설정
개발 시 임시로 CSRF 미들웨어 주석 처리 가능:
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # 주석 처리
    ...
]
```

---

## 앱 개발

### 1. 모델 정의
```python
# blog/models.py
from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
```

### 2. 앱 등록
```python
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # 앱 추가
]
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 데이터 조작

#### Django Shell 사용
```bash
python manage.py shell
```

```python
from blog.models import Question, Answer
from django.utils import timezone

# 데이터 생성
q = Question(subject='제목', content='내용', create_date=timezone.now())
q.save()

# 데이터 조회
Question.objects.all()
Question.objects.filter(id=1)
Question.objects.get(id=1)
```

---

## 모델과 데이터베이스

### 1. SQLite3 기본 사용

#### 특징
- 디스크 기반의 가벼운 데이터베이스
- Python에서 기본 제공
- 별도 서버 불필요
- 모바일 기기에서 널리 사용

#### 기본 조작
```python
import sqlite3

# 연결
con = sqlite3.connect("test.db")
cur = con.cursor()

# 테이블 생성
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")

# 데이터 삽입
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")

# 데이터 조회
cur.execute("SELECT * FROM PhoneBook;")
for row in cur:
    print(row)

# 커밋
con.commit()
```

### 2. Django 관리자 (Admin)

#### 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

#### 관리자 페이지 접속
```
http://127.0.0.1:8000/admin
```

#### 모델 등록
```python
# blog/admin.py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['subject', 'create_date']

admin.site.register(Question, QuestionAdmin)
```

---

## MySQL 연동

### 1. MariaDB 설치
1. https://downloads.mariadb.com/MariaDB/ 에서 다운로드
2. C:\mariadb에 압축 해제
3. 관리자 권한으로 CMD 실행

```bash
cd /mariadb/bin
mysql_install_db --datadir=C:\mariadb\data --service=mariaDBZip --port=3306 --password=1234
```

### 2. 데이터베이스 및 사용자 생성
```sql
mysql -u root -p --port=3306

CREATE DATABASE mydb default CHARACTER SET UTF8;
GRANT ALL PRIVILEGES ON mydb.* TO user01@localhost IDENTIFIED BY '1234';
EXIT;
```

### 3. Django 설정
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'user01',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. 필요한 라이브러리 설치
```bash
pip install pymysql
pip install mysqlclient
```

---

## MongoDB 연동

### 1. MongoDB 설치
1. https://www.mongodb.com/download-center 에서 다운로드
2. 환경변수 PATH에 추가: `C:\Program Files\MongoDB\Server\4.0\bin`
3. 데이터 디렉토리 생성: `c:\data\db`

### 2. MongoDB 서버 실행
```bash
mongod
```

### 3. MongoDB 기본 조작
```bash
mongo
```

```javascript
// 데이터베이스 생성/사용
use mydb

// 컬렉션 생성
db.createCollection('person')

// 데이터 삽입
db.person.insert({'name':'홍길동', 'age':26, 'gender':'m'})

// 데이터 조회
db.person.find()

// 데이터 수정
db.person.update({'name':'홍길동'}, {$set:{'age':40}})

// 데이터 삭제
db.person.remove({'name':'홍길동'})
```

### 4. Python-MongoDB 연동
```python
from pymongo import MongoClient

# 연결
client = MongoClient("mongodb://test:1234@127.0.0.1:27017/")
db = client.mydb

# 데이터 조회
rows = db.person.find()
for row in rows:
    print(row)

# 데이터 삽입
db.guestbook.insert({
    'id': 1,
    'title': '제목1',
    'contents': '내용1',
    'writer': '홍길동'
})
```

---

## 템플릿 시스템

### 1. 템플릿 디렉토리 설정
```bash
mkdir templates
mkdir templates/blog
```

### 2. 설정 파일 수정
```python
# config/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 템플릿 디렉토리 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 3. 템플릿 문법

#### 변수 출력
```html
{{ variable }}
{{ object.attribute }}
```

#### 조건문
```html
{% if condition %}
    <p>조건에 해당되는 경우</p>
{% elif condition2 %}
    <p>두 번째 조건에 해당되는 경우</p>
{% else %}
    <p>조건에 해당되지 않는 경우</p>
{% endif %}
```

#### 반복문
```html
{% for item in items %}
    <p>{{ forloop.counter }}: {{ item }}</p>
{% endfor %}
```

### 4. 템플릿 상속
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

```html
<!-- templates/blog/question_list.html -->
{% extends 'base.html' %}

{% block title %}질문 목록{% endblock %}

{% block content %}
    <h1>질문 목록</h1>
    {% for question in questions %}
        <div>{{ question.subject }}</div>
    {% endfor %}
{% endblock %}
```

### 5. 정적 파일 (Static Files)

#### 설정
```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

#### 사용
```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
<script src="{% static 'common.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## 폼 처리

### 1. Django Forms 사용

#### forms.py 생성
```python
# blog/forms.py
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
```

#### View에서 폼 처리
```python
# blog/views.py
from django.shortcuts import render, redirect
from .forms import QuestionForm

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('blog:index')
    else:
        form = QuestionForm()
    return render(request, 'blog/question_form.html', {'form': form})
```

#### 템플릿에서 폼 사용
```html
<!-- templates/blog/question_form.html -->
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h5>질문 등록</h5>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">저장</button>
    </form>
</div>
{% endblock %}
```

### 2. 페이징 (Pagination)

#### View에서 페이징 구현
```python
from django.core.paginator import Paginator

def index(request):
    questions = Question.objects.order_by('-create_date')
    paginator = Paginator(questions, 10)  # 페이지당 10개
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'questions': page_obj}
    return render(request, 'blog/question_list.html', context)
```

#### 템플릿에서 페이징 표시
```html
<!-- 페이징 처리 -->
<ul class="pagination">
    {% if questions.has_previous %}
        <li class="page-item">
            <a class="page-link" href="?page=1">처음</a>
        </li>
        <li class="page-item">
            <a class="page-link" href="?page={{ questions.previous_page_number }}">이전</a>
        </li>
    {% endif %}
    
    {% for page_number in questions.paginator.page_range %}
        {% if page_number == questions.number %}
            <li class="page-item active">
                <span class="page-link">{{ page_number }}</span>
            </li>
        {% else %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
            </li>
        {% endif %}
    {% endfor %}
    
    {% if questions.has_next %}
        <li class="page-item">
            <a class="page-link" href="?page={{ questions.next_page_number }}">다음</a>
        </li>
        <li class="page-item">
            <a class="page-link" href="?page={{ questions.paginator.num_pages }}">마지막</a>
        </li>
    {% endif %}
</ul>
```

---

## 사용자 인증

### 1. 앱 생성
```bash
django-admin startapp common
```

### 2. 설정 파일 수정
```python
# config/settings.py
INSTALLED_APPS = [
    # ... 기존 앱들
    'common',
]

# 로그인 성공 후 이동할 URL
LOGIN_REDIRECT_URL = '/'

# 로그아웃 성공 후 이동할 URL
LOGOUT_REDIRECT_URL = '/'
```

### 3. URL 설정
```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('', include('blog.urls')),
]
```

```python
# common/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

### 4. 로그인 템플릿
```html
<!-- templates/common/login.html -->
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row justify-content-center">
        <div class="col-4">
            <h4>로그인</h4>
            <form method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label for="username">사용자명:</label>
                    <input type="text" class="form-control" name="username" id="username" required>
                </div>
                <div class="form-group">
                    <label for="password">비밀번호:</label>
                    <input type="password" class="form-control" name="password" id="password" required>
                </div>
                <button type="submit" class="btn btn-primary">로그인</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

### 5. 네비게이션 바에 로그인/로그아웃 추가
```html
<!-- templates/navbar.html -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="/">Django Blog</a>
        <div class="navbar-nav ml-auto">
            {% if user.is_authenticated %}
                <a class="nav-link" href="{% url 'common:logout' %}">{{ user.username }} (로그아웃)</a>
            {% else %}
                <a class="nav-link" href="{% url 'common:login' %}">로그인</a>
            {% endif %}
        </div>
    </div>
</nav>
```

---

## Restful API

### 1. JSON 처리
```python
import json

# Python Dictionary를 JSON으로 변환
data = {
    'id': 152352,
    'name': '홍길동',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

# JSON 인코딩
json_string = json.dumps(data)

# JSON 디코딩
dict_data = json.loads(json_string)
```

### 2. API View 구현
```python
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["GET"])
def api_question_list(request):
    questions = Question.objects.all()
    data = []
    for question in questions:
        data.append({
            'id': question.id,
            'subject': question.subject,
            'content': question.content,
            'create_date': question.create_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'questions': data})

@require_http_methods(["POST"])
def api_question_create(request):
    data = json.loads(request.body)
    question = Question.objects.create(
        subject=data['subject'],
        content=data['content'],
        create_date=timezone.now()
    )
    return JsonResponse({
        'id': question.id,
        'subject': question.subject,
        'content': question.content
    })
```

---

## 배포

### 1. Git 설정

#### Git 초기화
```bash
cd /project/mysite
git init
```

#### .gitignore 파일 생성
```
# .gitignore
.idea
db.sqlite3
*.pyc
__pycache__
```

#### 커밋
```bash
git add --all .
git commit -m "Initial commit"
```

### 2. PythonAnywhere 배포

#### 1. 계정 생성
1. https://www.pythonanywhere.com/ 접속
2. Price & Signup 클릭하여 회원가입

#### 2. 배포 환경 설정
```bash
# PythonAnywhere 콘솔에서 실행
mkdir project
cd project
virtualenv --python=python3.7 myvenv
source myvenv/bin/activate
pip install django
```

#### 3. 프로젝트 업로드
- 로컬에서 작성한 코드를 PythonAnywhere에 업로드
- Web 탭에서 Django 애플리케이션 설정

---

## 마무리

이 가이드는 Django 프레임워크를 사용한 웹 애플리케이션 개발의 전체적인 흐름을 다룹니다. 각 섹션은 독립적으로 학습할 수 있도록 구성되어 있으며, 실제 프로젝트에서 참고할 수 있는 코드 예제를 포함하고 있습니다.

### 추가 학습 자료
- Django 공식 문서: https://docs.djangoproject.com/
- Django Girls 튜토리얼: https://tutorial.djangogirls.org/
- MDN Django 튜토리얼: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

### 주요 명령어 정리
```bash
# 프로젝트 생성
django-admin startproject myproject

# 앱 생성
python manage.py startapp myapp

# 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 슈퍼유저 생성
python manage.py createsuperuser

# 서버 실행
python manage.py runserver

# 셸 실행
python manage.py shell
```

