# 주민번호를 입력
# 1, 3 -> 남자 아니면 여자

jumin=input("주민번호를 입력하세요").split('-')#080515-3612436
if jumin[1][0] == '1' or jumin[1][0] == '3':
    print("남자")
else:
    print("여자")


    # 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라
num1 = int(input("첫 번째 숫자를 입력하세요. : "))
num2 = int(input("두 번째 숫자를 입력하세요. : "))
num3 = int(input("세 번째 숫자를 입력하세요. : "))
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2) 
else:    
    print(num3)