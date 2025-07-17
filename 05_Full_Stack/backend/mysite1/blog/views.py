from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse 
# Create your views here.

# HttpRequest: 클라이언트(브라우저 등)에서 서버로 전달되는 모든 요청 정보가 담긴 객체
# HttpResponse: 서버에서 클라이언트로 보낼 응답 데이터를 담는 객체
# 웹에서 특정 URL로 요청이 들어오면, 해당 URL에 연결된 view 함수가 호출됨

def index(request):
    # /blog/로 접속 시 단순 텍스트 응답 반환 (테스트용)
    return HttpResponse("Hello Django");

# 이 함수와 URL을 연결하려면 urls.py에서 path를 지정해야 함
# 예: http://127.0.0.1:8000/blog → blog/views.py의 index 함수 호출

from .models import Blog 
from django.core import serializers

# 블로그 글 목록을 JSON으로 반환 (API 용)
# 예: http://127.0.0.1:8000/blog/list
# 프론트엔드(React, Vue 등)에서 AJAX로 호출할 때 사용 가능

def getList2(request):
    dataSet = list(Blog.objects.values())
    # Blog 모델의 모든 데이터를 딕셔너리 리스트로 변환
    # (참고) Django의 serializers.serialize는 쿼리셋만 지원, values()는 딕셔너리 리스트 반환
    # data = serializers.serialize("json", dataSet)  # 쿼리셋 직렬화 예시(주석처리)
    return JsonResponse(dataSet, safe=False, json_dumps_params={'ensure_ascii': False})

# 블로그 글 목록을 HTML로 렌더링 (템플릿 렌더링)
def getList(request):
    dataSet = list(Blog.objects.values())
    # blog/blog_list.html 템플릿에 blogList라는 이름으로 데이터 전달
    return render(request, "blog/blog_list.html", {"blogList":dataSet})

# 블로그 글 상세보기 (id로 단일 데이터 조회)
def view(request, id ):
    print("id = ", id)
    # Blog 모델에서 id(PK)로 객체 1개 조회 (없으면 예외 발생)
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog_view.html", {"blog":blog})

# 글쓰기 페이지 이동 (빈 폼 렌더링)
def write(request): #blog_write.html페이지로 이동 
    return render(request, "blog/blog_write.html")

# forms.py에서 BlogForms 클래스 import (동일 디렉토리)
from .forms import BlogForms 
from django.utils import timezone  
from django.shortcuts import redirect

# 블로그 글 저장 (POST 요청 처리)
def save(request):
    form = BlogForms(request.POST) # 폼 데이터로 BlogForms 객체 생성
    # form.fieldList에 있는 title, content 등 필드에 form태그의 값이 자동 매핑됨
    blogModel = form.save(commit=False) # DB 저장 전 임시 Blog 객체 생성
    # 추가 필드(작성일, 조회수 등) 직접 할당
    blogModel.wdate = timezone.now() 
    blogModel.hit = 0 
    blogModel.save() # 실제 DB에 저장

    # 저장 후 글 목록 페이지로 리다이렉트
    # 직접 blog_list 함수 호출이 아니라, 클라이언트가 새로 요청하도록 redirect 사용
    return redirect("blog:blog_list")
# app_name 등록 blog 
# name="blog_list"  