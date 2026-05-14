# 숫자 입력 -> 출력 반복, 0 입력 시 종료
# while True:  
#     num = int(input("숫자를 입력하세요 : "))
#     if num == 0:
#         print("종료합니다.")
#         break
#     print("입력한 숫자 :", num)

menu=["쫄면","김밥","냉면","오뎅"]
b=input("메뉴 선택 : ")
while b in menu:
    print(b,"을 선택하셨습니다.")
    b=input("메뉴 선택 : ")
# while문은 조건이 참인 동안 계속 반복 거짓으로 변경되는 문장이 나와야 탈출