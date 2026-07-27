import math as ma # math 모듈 : 수학 계산 함수
import random

num = 25

print("제곱근 : ",ma.sqrt(num))
print("2의 3제곱",ma.pow(2,3))
print("원주율 : ",ma.pi)

student = ["홍길동","권율","전정우"]

sel = random.choice(student)
# random.choice: 리스트 안에서 무작위 선택
dice = random.randint(1,6)
#random.randit(1,6) : 1 ~ 6 까지 안에서 무작위 추출

print("발표학생 추첨 : ",sel)
print("주사위 숫자 : ",dice)