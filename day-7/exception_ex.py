# exception_ex.py

try:
    num = int(input("숫자 입력"))
    res = 10/num
except ValueError: # except : 예외발생시 처리(값 오류)
    print("숫자가 아닙니다")
except ZeroDivisionError: # 0으로 나눌 수 없음
    print("0으로 나눌 수 없음")
except Exception as e: # 그외 나머지 예외인 경우
    print("에러메시지")
else: # 정상적인 경우
    print("결과 : ",res)
finally: # 공통적 수행 (무조건 수행)
    print("종료")