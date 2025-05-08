
# TODO: 정수를 5개 입력받아서 합계를 구하라.
sum = 0 # 합계를 저장할 변수
for i in range(5):
    num = int(input("정수를 입력하세요 : "))
    sum += num
print("합계 : ", sum)

# TODO: 숫자를 10개 입력받아서 각각 짝수와 홀수의 합과 평균을 구하라.
even_sum = 0 # 짝수 합
even_count = 0 # 짝수 개수
odd_sum = 0 # 홀수 합
odd_count = 0 # 홀수 개수

for i in range(10):
    num = int(input(f"{i+1}번째 숫자를 입력하세요 : "))

    if num % 2 == 0:    # 짝수인 경우
        even_sum += num
        even_count += 1
    else:
        odd_sum += num  # 홀수인 경우
        odd_count += 1

# 평균 계산(개수가 0일 수 있기에 나눌 떄 확인)
if even_count > 0:
    even_avg = even_sum / even_count
else:
    even_avg = 0

if odd_count > 0:
    odd_avg = odd_sum / odd_count
else:
    odd_avg = 0

print("짝수의 합 : ", even_sum, "짝수의 평균 : ", even_avg)
print("홀수의 합 : ", odd_sum, "홀수의 평균 : ", odd_avg)


# NOTE 클린 코드로 작성한  문제 1, 2
# # 정수 5개 입력받아서 합계를 구하는 코드 (클린 코드)

# total = 0  # 합계 저장 변수

# for index in range(5):
#     number = int(input(f"{index + 1}번째 정수를 입력하세요: "))
#     total += number  # 입력받은 숫자를 합계에 더함

# print("총 합계:", total)

# # 숫자 10개 입력받아서 짝수/홀수의 합과 평균 구하기 (클린 코드)

# even_sum = 0        # 짝수 합
# even_count = 0      # 짝수 개수
# odd_sum = 0         # 홀수 합
# odd_count = 0       # 홀수 개수

# for index in range(10):
#     number = int(input(f"{index + 1}번째 숫자를 입력하세요: "))

#     if number % 2 == 0:            # 짝수인 경우
#         even_sum += number
#         even_count += 1
#     else:                          # 홀수인 경우
#         odd_sum += number
#         odd_count += 1

# # 평균 계산 (0으로 나누는 상황 방지)
# even_average = even_sum / even_count if even_count > 0 else 0
# odd_average = odd_sum / odd_count if odd_count > 0 else 0

# print("\n[결과]")
# print(f"짝수 합계: {even_sum}, 짝수 평균: {even_average}")
# print(f"홀수 합계: {odd_sum}, 홀수 평균: {odd_average}")
