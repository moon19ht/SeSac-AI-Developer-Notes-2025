from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator # Paginator import
from .models import Score # Score 모델이 있다고 가정

"""
[페이징 시스템 개념 및 실무 설명]

- 대용량 데이터 조회 시 모든 데이터를 한 번에 메모리로 불러오면 서버가 느려지거나 장애가 발생할 수 있음
- 이를 방지하기 위해 '페이징'을 사용: 한 번에 일부 데이터(한 페이지 분량)만 조회
- MySQL 등 DB에서는 LIMIT, OFFSET을 활용해 원하는 범위만 쿼리로 가져옴
- Django에서는 Paginator 클래스를 통해 페이징 처리를 쉽게 구현 가능
- Paginator는 전체 데이터 개수, 페이지 수, 현재 페이지, 이전/다음 페이지 존재 여부 등 다양한 정보를 자동으로 제공
- 실무에서는 직접 페이징 로직을 구현하지 않고, 프레임워크의 기능을 적극 활용하는 것이 효율적임

[SPA(Single Page Application)와 페이징]
- SPA는 React, Vue 등 프론트엔드 프레임워크에서 많이 사용
- 화면 전체가 아닌 일부만 동적으로 갱신하여 UX가 뛰어남
- SPA에서는 전통적인 페이징 대신 무한 스크롤(Infinite Scroll) 방식이 자주 쓰임

[지연 생성(Lazy Loading) 패턴]
- 객체를 선언만 해두고, 실제로 필요할 때 메모리 할당 및 초기화를 수행하는 방식
- 상호 참조, 무거운 초기화 비용이 있는 경우에 유용
"""

def index(request):
    # score:index로 접근 시 score_list로 리다이렉트
    return redirect("score:score_list")

"""
C# 등에서의 DB 커넥션 풀 관리, 쿼리 로그 주의사항 등 실무 팁
- 웹서버 운영 시 쿼리 로그는 디버깅 용도로만 사용, 운영 환경에서는 비활성화 권장
- ORM(Object-Relational Mapping) 도입으로 페이징, CRUD 등 반복 로직을 자동화하여 개발 효율성 향상
"""

def list(request): # 여러 데이터 조회 및 페이징
    # [1] 전체 데이터 쿼리셋 준비 (최신순 정렬)
    scoreList = Score.objects.all().order_by('-id') 
    # 주의: 쿼리셋은 실제로 데이터를 메모리에 올리지 않고, 이후 슬라이싱/페이징 시점에 쿼리가 실행됨

    # [2] Paginator 객체 생성 (한 페이지에 10개씩 보여줌)
    paginator = Paginator(scoreList, 10) 
    # Paginator는 전체 데이터 개수, 페이지 수, 현재 페이지 등 정보를 자동 계산

    # [3] GET 요청에서 'page' 파라미터 추출 (없으면 1페이지)
    page_number = request.GET.get('page')
    # 예: /score/list?page=2 → 2페이지 데이터 요청

    # [4] 해당 페이지의 데이터만 쿼리로 가져옴 (실제 DB 쿼리 실행)
    page_obj = paginator.get_page(page_number) 
    # page_obj에는 현재 페이지의 Score 객체 목록, 페이지 정보 등이 포함됨

    # [5] 템플릿에 전달할 컨텍스트 구성
    context = {
        "page_obj": page_obj, # 템플릿에서 page_obj를 통해 데이터와 페이징 정보 모두 접근 가능
        "title": "성적처리",
    }
    return render(request, "score/score_list.html", context)


def view(request, id): # 단일 데이터 상세 조회
    # id(PK)로 Score 객체를 조회, 없으면 404 에러 반환
    scoreModel = get_object_or_404(Score, pk=id)
    return render(request, "score/score_view.html", {'item':scoreModel})


def write(request):
    # 빈 ScoreForm 객체 생성 (입력 폼 렌더링)
    scoreform = ScoreForm() 
    # context에 'modify':False를 추가하여 템플릿에서 등록/수정 모드 구분
    context ={'form':scoreform, 'modify':False}
    return render(request, "score/score_write.html",context  )

from .models import Score 
from .forms import ScoreForm 

def save(request): # 새 데이터 저장
    # POST 요청(폼 제출)일 때만 저장 로직 실행
    if request.method =="POST":
        scoreform = ScoreForm(request.POST)
        scoreModel = scoreform.save(commit=False) # DB 저장 전 임시 객체 생성
        # 총점, 평균, 작성일시 등 추가 필드 계산
        scoreModel.total = scoreModel.kor + scoreModel.eng + scoreModel.mat
        scoreModel.avg = scoreModel.total/3 
        scoreModel.wdate = timezone.now() 
        scoreModel.save() # 실제 DB에 저장
    return redirect("score:score_list")


def update(request, id): # 기존 데이터 수정
    # id로 기존 Score 객체 조회
    scoreModel = get_object_or_404(Score, pk=id)
    if request.method=="POST":
        # 폼에서 전달된 데이터로 ScoreForm 생성
        scoreform = ScoreForm(request.POST)
        scoreModel = scoreform.save(commit=False)
        # 총점, 평균, 작성일시 등 갱신
        scoreModel.total = scoreModel.kor + scoreModel.eng + scoreModel.mat
        scoreModel.avg = scoreModel.total/3 
        scoreModel.wdate = timezone.now() 
        scoreModel.save()
        return redirect("score:score_view", pk=scoreModel.id)
    else:
        # GET 요청: 기존 데이터로 폼을 채워서 렌더링
        form = ScoreForm(instance=scoreModel)
    return render(request, 'score/score_write.html', {'form':form, 'modify':True, 'id':id})
    