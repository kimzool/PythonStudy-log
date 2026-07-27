# try:
    # 오류가 나지 않기위해 시험해보는 실행문
# except:
    # 오류가 발생했을때 실행
# else:
    # 오류가 발생하지 않을때 실행
# finally:
    # 오류 여부와 관계없이 항상 수행

try :
    num = int(input("숫자를 입력하세요.."))
    res = 100/num
except ValueError:
    print("숫자를 입력하세요")
except ZeroDivisionError:
    print("0을 제외한 숫자를 입력하세요..")
else:
     print("100을 ",num,"으로 나눈 값 : ",res)

finally:
   print(" 실행 끝 ")