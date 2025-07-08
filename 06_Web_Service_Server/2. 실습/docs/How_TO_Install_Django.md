# Django 설치 및 프로젝트 구성 가이드

데이터베이스를 `mysql`로 옮기기 <br>
함수뷰를 사용해서 정밀하게 데이터베이스 제어 <br>
`form`태그를이용해서 게시판에 글쓰기 페이징까지 <br>

## 1. 가상환경 만들기

```bash
conda create --name mysite
conda activate mysite 
```

## 2. Django 설치

```bash
pip install django 
```

## 3. 웹 프로젝트를 놓을 폴더로 이동 

```bash
(mysite)c:/users/user>cd \django_workspace
```

## 4. 프로젝트 작성 

```bash
django-admin startproject mysite
```

## 5.경로로 이동

```bash
cd mysite        
```

## 6. DB에 반영할 마이그레이션 정보 만들기

```bash
# 모델 클래스를 수정할때마다 호출해야한다. 
python manage.py makemigrations 
```

## 7. 실제 DB에 반영

```bash
python manage.py migrate 
``` 

## 8. 서버 실행
> 웹 브라우저에서 **http://127.0.0.1:8000/**

```bash
python manage.py runserver 
```

## 9. APP 추가 - 자동으로 코드를 추가해준다.

```bash
django-admin startapp blog 
```

```
blog/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
 ```

## 10. urls.py파일만들기

> config 폴더아래의 urls.py를 복사해서 붙여넣기를 한다.
> urls.py 파일은 직접생성해야 한다. 


```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("test1", views.test1),
    path("test2", views.test2),
    path("test3/<xvalue>/<yvalue>", views.test3),
    path("test4", views.test4),
    path("test5", views.test4),
]
```


## 11. config/urls.py 내용 수정하기
    

```python
from django.contrib import admin
from django.urls import path, include
from blog import views 
urlpatterns = [
        path("admin/", admin.site.urls),
        # path("blog/", views.index)
        path("blog/", include("blog.urls")),
]
```


## 12. config/settings.py 수정하기

```python
INSTALLED_APPS = [
    "blog.apps.BlogConfig",  # APP 등록
    "board.apps.BoardConfig", # APP 등록

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

## 13. views.py 파일 수정하기

```python
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello Django")

def test1(request):
    return HttpResponse("test1")

def test2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'Unknown')
    return HttpResponse(f'<h1>{ua}</h1>')

# http://127.0.0.1:8000/test3/4/5
def test3(request, xvalue, yvalue):
    result = int(xvalue) + int(yvalue)
    return HttpResponse(f"{xvalue} + {yvalue} = {result}")

# http://127.0.0.1:8000/test4?x=4&y=5
def test4(request):
    xvalue = int(request.GET.get("x", 0))
    yvalue = int(request.GET.get("y", 0))
    result = xvalue + yvalue
    return HttpResponse(f"{xvalue} + {yvalue} = {result}")

# POST 방식으로 /test5 요청
def test5(request):
    if request.method == "POST":
        xvalue = int(request.POST.get("x", 0))
        yvalue = int(request.POST.get("y", 0))
        result = xvalue + yvalue
        return HttpResponse(f"{xvalue} + {yvalue} = {result}")
    else:
        return HttpResponse("Error: Only POST method is allowed.")
```

## 14. models.py 파일만들기

```python
from django.db import models
```

### Create your models here. 테이블과 1:1매핑된다.
Django에서 모델(models.Model)을 정의할 때 기본적으로 `id`라는 이름의 `AutoField`가 자동으로 생성되어 `Primary Key` 역할을 한다.<br>
별도로 지정하지 않아도 자동 증가되는 정수형 `PK`가 생성된다.


```python
from django.db import models

class Question(models.Model): 
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # 자동으로 Question.id 필드와 묶인다.
    # 변수명은 보통 클래스명을 소문자로 바꿔서 사용한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content
```

## 15. Database 가져오기
`파일명 blog/view.py`

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer


def getData1(request):
    question_list = Question.objects.order_by('-create_date')
    return HttpResponse(question_list)


def getData2(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()  # 모든 Answer 데이터 가져오기
    return render(request, 'blog/qna_list1.html', {
        'questions': questions,
        'answers': answers
    })


def getData3(request):
    questions = Question.objects.all().prefetch_related('answer_set')  # 쿼리 최적화
    return render(request, 'blog/qna_list2.html', {'questions': questions})
```

## 16. 템플릿 추가하기 

```python
import os

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates')
            ],
        "APP_DIRS": True,
        "OPTIONS": 
        {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
```


> filename: /templates/blog/qna_list1.html

```html
<h2>Question List</h2>
<ul>
  {% for question in questions %}
    <li>
      <strong>{{ question.subject }}</strong><br>
      {{ question.content }}<br>
      작성일: {{ question.create_date }}
    </li>
  {% endfor %}
</ul>
```
---

```html
<h2>Answer List</h2>
<ul>
  {% for answer in answers %}
    <li>
      <strong>질문: {{ answer.question.subject }}</strong>
      <br>답변: {{ answer.content }}
      작성일:{{ answer.create_date }}
    </li>
  {% endfor %}
</ul>
```

---

**filename: /templates/blog/qna_list2.html**
<!-- qa_grouped.html -->

```html
<h2>질문과 답변 목록</h2>
<ul>
  {% for q in questions %}
    <li>
      <strong>Q: {{ q.subject }}</strong><br>
      {{ q.content }}<br>
      작성일: {{ q.create_date }}
      <ul>
        {% for a in q.answer_set.all %}
          <li>A: {{ a.content }} ({{ a.create_date }})</li>
            {% empty %}
          <li>답변 없음</li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}
</ul>
```

## 17. 새로운 앱 추가하기 

```bash
django-admin startapp board 
```

모든 환경설정은 `config/settings.py` 파일에서 
원래있던 내용은 주석처리를 한다.

```python
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'user01',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
```

#### DB가 바뀌면 mysqlclient 설치해야 한다.

```bash
# Django 에서 지원하는 라이브러리
pip install mysqlclient 
```

먼저, 테이블을 생성해야 한다. 

```bash
python manage.py makemigrations
python manage.py migrate 
mysql -u root -p 
```

---

```sql
use mydb;
show tables;
grant all privileges on mydb.*
to user01@localhost identified by '1234';
```

---

```
c:/django_workspace
      ㄴmyhome2
           ㄴ manage.py 
           ㄴ config
                 ㄴ settings.py  # 이 두 개의 파일만 건드린다
                 ㄴ urls.py 
```

새로운 앱을 추가하자 - board (CRUD-create read update delete)

```bash
django-admin startapp board
```
`board` 라는 앱이 만들어진다. 


### 17-1. APP 등록 (settings.py)

```python
INSTALLED_APPS = [
    'board.apps.BoardConfig', 
    # 이 부분에 현재 등록한 앱정보를 등록 해야한다.
```
`board` 라는 앱을 만들면, board 폴더 아래에 `apps.py` 파일이 만들어지고 <br>
`BoardConfig` 클래스가 만들어진다. 


```
board 
  ㄴapps.py
```
`BoardConfig` 앱의이름이 
`board.apps.BoardConfig` 앱이름(폴더명).파일명.클래스명 


### 17-2. 모델클래스를 먼저 만들고 

**c:/django_workspace/myhome2/board/models.py**
 
```python
class Board(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용")
    wdate = models.DateTimeField("작성일", auto_now=False, auto_now_add=False) 
    writer = models.CharField("작성자", max_length=50) 
    hit = models.IntegerField("조회수")

# __str__ 함수 overriding 
def __str__(self):
    self.title + " " + self.writer
    return
``` 

모델클래스만들면 `python manage.py makemigrations board`아래에 `migrations` 폴더만들고 `0001_inital.py` 파일을 만든다.

```bash
python manage.py migrate
```
위의 파일을 기반으로 실제 데이터베이스에 테이블을 만드는 명령어는 `migrate`이다 

### 17-3. urls.py 파일을 만들어서 
**config/urls.py**
> 수정 `/mysite/board/urls.py` 

```python
from django.contrib import admin
from django.urls import path 
# . 현재 나와 같은 경로에 있는 views.py 를 import 해라 
from . import views 

app_name = 'board'  # APP 이름 부여. 
# 맨처음 django-admin startapp board 이름
# url와 view를 연결짓는 부분이다. 

urlpatterns = [
    path('', views.index)  
    # path함수가 url과  view의 함수나 클래스를 연결시킨다. 
]
```
### 17-4. myhome2/urls.py 수정

```python
from django.contrib import admin
from django.urls import path
from django.urls import include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')) 
]
```

### 17-5. board/views.py  index함수 추가하기

```bash
python manage.py runserver
```
`http://127.0.0.1:8000/board`

### 17-6.

```markdown 
c:/django_workspace/myhome2
    ㄴtemplates 폴더를 만들고 
        ㄴ board 
            ㄴboard_list.html
            ㄴboard_view.html
            ㄴboard_write.html
```
`settings.py` 파일안에 `TEMPLATES`에 다음 코드 추가  

```python
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
            ],
```

### 17-7. 사이트에서 제공해주는 `admin`을 사용해보자 

```bash
python manage.py createsuperuser
```

```
admin/qwer1234   
admin
@myhome2.com 
```

`http://127.0.0.1:8000/admin`

### 17-8.admin 쪽에서 board_board  테이블 보이게 
**board/admin.py**

```python
from .models import Board 
class BoardAdmin(admin.ModelAdmin):
    search_fields =['title']
    admin.site.register(Board, BoardAdmin)
```

### 17-9. 데이터 추가 

```sql
ALTER TABLE board_board convert to charset utf8;
delete from board_board; 
select * from board_board;
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
insert into board_board (title, writer, contents, wdate, hit)
values('제목1', '작성자', '내용1', now(), 0);
...
```


### 17-10.views.py파일에서 함수뷰를 사용해서 데이터를 가져오기 

테스트방법 제공. 서버끄고, 가상화 작동중인 상태로

```bash
(mysite2)C:/django_workspace/myhome2
python manage.py shell 
```

콘솔창에서

```python
from board.models import Board
Board.objects.all()
```
테이블에 있는 모든 데이터를 갖고 있다.
데이터가 100만건 있으면 100만건.
우리가 원하는건 페이지를 지정하면 지정한 페이지 건수만 와야 한다.
`limit`라는 구문을 사용해야 한다.

```
queryset = Board.objects.all() 
str(queryset.query)
# 직접연결객체를 안만들고 장고가 이미 연결객체를 갖고 있어서 이걸 가져온다 
```
```python
from django.db import connection
cursor = connection.cursor() 
cursor.execute('select * from board_board limit 0,5 ')
board_list = cursor.fetchall()
print(board_list) # meta 정보 
print(cursor.description)
```

```
(('id', 3, 3, 11, 11, 0, 0), ('title', 253, 7, 600, 600, 0, 0), ('contents', 252, 7, -1, -1, 0, 0), ('wdate', 12, 26, 26, 26, 6, 0), ('writer', 253, 9, 150, 150, 0, 0), ('hit', 3, 1, 11, 11, 0, 0))
```

---

```python
columns = list()
for col in cursor.description:
    print(col[0]) # ('id', 3, 3, 11, 11, 0, 0)
    columns.append(col[0])

columns = [ col[0] for col in cursor.description ]
print(columns) # ['id', 'title', 'writer', 'contents'] 

cursor.execute('select * from board_board limit 0,5 ')
for row in cursor.fetchall():
    print(row)
```

```
['id', 'title', 'writer', 'contents'] # columns 

(254, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
(255, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
(256, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
(257, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
(258, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
```

---

```python
a = ['id', 'title', 'contents', 'wdate', 'writer', 'hit']
row = (254, '제목1', '내용1', datetime.datetime(2020, 8, 24, 15, 21, 45), '작성자', 0)
mydict = dict(zip(a, row))
print(mydict)
for key in mydict:
    print(key, mydict[key])

cursor.execute('select * from board_board limit 0,5 ')
board_list = [dict( zip(columns, row)) for row in cursor.fetchall()]
print(board_list)
```

Django 에서 사용하는 `mysqlclient` 라이브러리가 무조건 `tuple` 타입으로 데이터를 가져온다. 

```python
# DB에서 가져온 데이터를 tuple->dict 으로 바꾸는 함수 
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    # 테이블의 열에대한 정보를 가져와야 한다 
    columns = [ col[0] for col in cursor.description ]
    # 간략화한  list 
    return [ dict( zip(columns, row)) for row in cursor.fetchall()]
    # columns = ['id', 'title', 'writer', 'wdate', 'hit', 'contents']
    # ((1, '제목1', '작성자', '2020-08-24', 0), )
    # [{'id':'1', 'title':'제목1', ,,,,}
```
**board/views.py**
```python
from django.db import connection

def list(request):
    sql = '''
        select id, title, writer, contents, hit, wdate from board_board limit 0, 10
        '''
    # limit  시작위치, 개수 
    cursor = connection.cursor()
    cursor.execute(sql)
    board_list = dictfetchall(cursor)
    context = {'board_list':board_list}
    return
 render(request, 'board/board_list.html', context)
 ```