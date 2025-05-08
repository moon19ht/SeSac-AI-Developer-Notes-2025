
# TODO 과제1 정수를 받아서 짝수이면 True 홀수이면 False를 반환하는 함수
def Which_One_OddEvenNum(num):
    # 정수를 받아 짝수이면 True, 아니면 False를 반환
    return num % 2 == 0

# 정수 입력
Number = int(input("정수를 입력하시오 : "))

# 홀 짝 판별 출력
print(Which_One_OddEvenNum(Number))

# TODO 과제2 윤년(366일)이 오는 주기는 4년마다이다. 
# 함수를 만들어서 윤년이면 True, 아니면 False를 출력하라
def Leap_Year(year):
    # 4년마다 윤년(True/False)
    return year % 4 == 0  

# 연도 입력
Year = int(input("연도를 입력하세요 : "))

# 윤년 판별 출력
print(Leap_Year(Year))

# NOTE  참고: 리턴값만 활용해서 코드를 짜도 된다.

# 윤년 계산 방식 확장 (선택사항)
# 질문에 “4년마다”라고만 되어 있지만, 실제 그레고리력 Gregorian calendar에서는
# 4로 나누어떨어지면 윤년
# 단, 100으로 나누어떨어지면 평년
# 400으로 나누어떨어지면 다시 윤년

# 예시 코드
# def is_leap_gregorian(year):
#     """
#     그레고리력 기준 윤년 판단:
#       • 4로 나누어떨어지고
#       • (100으로 나누어떨어지지 않거나 400으로 나누어떨어질 때)
#     """
#     return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# # --- 호출부 ---
# y = int(input("연도를 입력하세요: "))
# print(is_leap_gregorian(y))
