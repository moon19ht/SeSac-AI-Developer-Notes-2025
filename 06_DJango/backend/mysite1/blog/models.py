from django.db import models

"""
Django 모델 생성 가이드
- 반드시 models.Model을 상속받아야 함
- id 필드는 자동으로 생성됨
- ORM(Object-Relational Mapping): 객체지향식 데이터베이스 접근 방식
  장점: SQL 쿼리 작성 불필요
  단점: 복잡한 JOIN이나 서브쿼리가 많을 때 성능 저하 가능
  권장: 테이블 10개 미만의 소규모 프로젝트에 적합
- Spring의 Entity 클래스와 동일한 역할
- 모델 기반 테이블 생성을 위해서는 settings.py의 INSTALLED_APPS에 앱 등록 필요
  예: 'blog.apps.BlogConfig'

Django Forms 활용
- HTML form의 name 속성값을 views.py에서 개별적으로 처리하는 대신
  forms.py 파일을 생성하여 자동 직렬화 처리
- HTML → 직렬화 → forms 변수에 자동 매핑
"""
class Blog(models.Model):
    title = models.CharField("제목", max_length=200) 
    contents = models.TextField("내용") 
    writer = models.CharField("작성자", max_length=200) 
    wdate = models.DateTimeField("작성일", auto_now=True) 
    hit = models.IntegerField("조회수")

    def __str__(self):
        return f"${self.title} ${self.writer}" 
    