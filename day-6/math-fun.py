# 내장함수
# len(길이)
# str(문자열)
# list(리스트) tuple(튜플)
# strip(공백제거)
# del(삭제)
# type(타입)
# input(입력)
# range(범위)

res=divmod(11,3)
print(res) #3, 2 ,(몫(//), 나머지(%))
print(abs(-5)) #절대값
print(pow(4,2)) #거듭제곱(제곱) 4**2
print(max(10,20,30)) #최댓값
print(min(10,20,30)) #최솟값
print(round(23.89)) #반올림

import math # -> math를 무조건 붙여야함 #수학(math) 관련 함수 제공하는 모듈
# from math import * 
#math 모든 함수를 네임스페이스에 가져옴
# #내림
print(math.floor(24.9)) #24 <-외장함수
print(math.floor(24.9)) #24 <-외장함수
# #올림
print(math.ceil(24.1)) #25
print(math.sqrt(16)) #제곱근
print(math.factorial(5)) #팩토리얼 5! = 5*4*3*2*1
print(math.pi) #원주율