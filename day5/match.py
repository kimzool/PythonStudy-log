num1=int(input("3의 배수를 입력하세요 : "))
num2=int(input("5의 배수를 입력하세요 : "))
match num1%3, num2%5:
    case 0,0:
        print("num1은 3의 배수 num2는 5의 배수")
    case 0,_:
        print("num1은 3의 배수 num2는 오류")
    case _,0:
        print("num1은 오류 num2는 5의 배수")
    case _,_:
        print("둘다 오류")