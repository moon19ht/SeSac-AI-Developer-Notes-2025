"""
문제3) 철수가 식료품점에 가서 과일을 샀다 사과와 배를 샀는데 사과는 
      한개에 5000 원이고 배는 10000원이다. 각각 사과와 배의 개수를 
      입력받아 총금액을 구하는 프로그램을 작성하시오
"""

#변수 받기
apple = int(input("사과의 개수는? "))
banana = int(input("배의 개수는? "))

#계산
apple_price = apple * 5000
banana_price = banana * 10000

#결과
print("총 금액은", apple_price + banana_price, "원입니다.")