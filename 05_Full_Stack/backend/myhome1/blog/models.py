from django.db import models

# 데이터베이스와 연동 - 데이터베이스 스키마를 여기 정의하면
# 그대로 데이터베이스 테이블을 직접 만들어준다
# 반드시 models.Model을 상속받아야 한다
# ORM(Object-Relational Mapping) 기법 - 객체 관계형 매핑
# 자동 쿼리 생성
class Blog(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용")
    wdate = models.DateTimeField("작성일", 
                    auto_now_add=True) # 객체 생성 시 자동 날짜시간 
    writer = models.CharField("작성자", max_length=40)
    hit = models.IntegerField("조회수")

    # 함수오버라이딩 
    def __str__(self):
       return  f"{self.title} {self.contents} {self.writer}"
