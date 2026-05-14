# #함수  
# def add(a, b):
#     return a + b

# n1 = int(input("첫번째 숫자 입력: "))
# n2 = int(input("두번째 숫자 입력: "))
# sum = add(n1, n2)  # 함수 호출, 리턴값을 저장
# print(sum)

# sum():합계
#len() : 길이
# 숫자리스트의 평균을 반환
# 1. 리스트의 합계를 구한다 (sum() 함수 활용 가능)
# 2. 리스트의 개수를 구한다 (len() 함수 활용 가능)
# 3. 합계를 개수로 나눈 값을 return한다
def avg():
    sum_score = sum(score_list) #합계
    count = len(score_list) #개수
    return sum_score / count #평균


score_list=[80, 90, 100, 50, 70]
#함수호출, 반환된 값을 저장 평균 출력
print(avg())