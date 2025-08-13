from django.shortcuts import render, redirect 
from django.http import HttpRequest, HttpResponse

# Create your views here.

from .models import Blog
def index(request):
    # 데이터를 전부 가져와라 
    return HttpResponse("Hello Django")

def list(request):
    blog_list = Blog.objects.all() 
    return render(request, "blog/blog_list.html", {"blogList":blog_list})

from .forms import BlogForms 
def write(request):
    form = BlogForms() # 객체 만들고 
    return render(request, 'blog/blog_write.html')

from django.utils import timezone 
def save(request): 
    # title = request.POST.get("title")
    form = BlogForms(request.POST)
    # 반환화는 객체가 model임 
    # form.save(commit=False)는 폼 데이터를 모델 인스턴스로 변환하지만 
    # 아직 데이터베이스에 저장하지는 않음
    # 이렇게 하면 추가적인 필드(wdate, hit)를 설정한 후 한번에 저장할 수 있음
    # 현재 title, writer, contents 필드만 설정된 상태
    blog = form.save(commit=False)
    blog.wdate = timezone.now() # wdate, hit 
    blog.hit=0 
    blog.save() 

    # 글쓰기 완료 후 목록 화면으로 리다이렉트 처리
    # list() 함수를 직접 호출하는 것이 아니라 HTTP 리다이렉트를 통해
    # 클라이언트가 새로운 요청을 보내도록 함
    # redirect("blog:list")는 urls.py의 app_name="blog"와 name="list"를 참조
    # 즉, path("list", views.list, name="list") 경로로 리다이렉트됨
    return redirect("blog:list")

def view(request, id):
    print("id", id)
    
    blog=Blog.objects.get(id=id)# DB에서 해당 아이디 읽어오기 
    blog.hit = blog.hit+1  # 조회수 증가하기  
    blog.save() 
    # print(blog)
    return render(request, "blog/blog_view.html", {"blog":blog}) 