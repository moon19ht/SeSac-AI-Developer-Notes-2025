from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

#HttpRequest -> 클라이언트가 보낸 정보를 받아오는 객체 
#HttpResponse -> 서버가 클라이언트로 보낼 정보를 저장해서 
#               클라이언트에서 전달될 객체 
#웹에서 정보를 요청하면 이 페이지가 호출된다. 
def index(request):
    return HttpResponse("Hello Django");

#이 함수와 url을 연결하는 작업이 필요하다 
#http://127.0.0.1/blog ==> blog/views.py파일의 index가 호출되게 한다
