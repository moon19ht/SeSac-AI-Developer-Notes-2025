"""
문제4) 거스름돈을 계산하기 : 10만원을 넣고 거스름돈 받기
      @예시
      물건 값 : 27560원
      거스름돈 : 72440원
      50000원 - 1장
      10000원 - 2장
      5000원 - 0장
      1000원 - 2장
      500원 - 0개
      100원 - 4개
      50원 - 0개
      10원 - 4개
      1원 - 0개
"""

# 물건값 입력받기
money = int(input("물건 값 : "))

# 거스름돈 계산
change = 100000 - money

# 거스름돈 계산
print("거스름돈 : ", change, "원")

# 지폐, 동전 개수 계산
print("50000원 - ", int(change / 50000), "장")
change %= 50000

print("10000원 - ", int(change / 10000), "장")
change %= 10000

print("5000원 - ", int(change / 5000), "장")
change %= 5000

print("1000원 - ", int(change / 1000), "장")
change %= 1000

print("500원 - ", int(change / 500), "개")
change %= 500

print("100원 - ", int(change / 100), "개")
change %= 100

print("50원 - ", int(change / 50), "개")
change %= 50

print("10원 - ", int(change / 10), "개")
change %= 10

print("1원 - ", int(change / 1), "개")
change %= 1

# # for문, if 문 응용

# # 물건값 입력받기
# money = int(input("물건 값 : "))

# # 거스름돈 계산
# change = 100000 - money
# print("거스름돈 : ", change, "원")

# # 지폐와 동전 단위 정의
# units = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

# # 지폐와 동전 개수 계산 및 출력
# for unit in units:
#     count = change // unit  # 해당 단위의 개수 계산
#     if unit >= 1000:
#         print(f"{unit}원 - {count}장")
#     else:
#         print(f"{unit}원 - {count}개")
#     change %= unit  # 나머지 계산

