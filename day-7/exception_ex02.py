# exception_ex02.py

fruits = ["사과","배","오렌지"] # 리스트 0~2

try:
    index = int(input("번호 입력 : "))
    if index <0 or index>=len(fruits):
         raise IndexError # 강제로 예외를 발생시킴
except IndexError:
    print("없는 인덱스입니다")
except ValueError:
        print("입력 오류")
except Exception as e:
    print("에러메시지",e)

else:
     print(fruits[index])
     
finally:
     print("종료")