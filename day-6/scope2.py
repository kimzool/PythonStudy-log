# 스코프(scope)
# 파이썬은 변수를 찾을때 가까운 영역부터 찾음
# LEGB 규칙 ( Local -> Enclosing -> Global -> Built-in) 
# Local -> 함수 내부 변수
# Enclosing -> 바깥 함수 변수
# Global -> 함수 밖 변수
# Built-in -> Python이 기본 제공하는 이름 (print,input....)
a = '홍길동' # 전역변수
b = 99 # 전역변수

def function1(): # 함수 1
    a = '이순신' # 중첩함수 변수
    c = [1 ,2 ,3]
    
    def function2(): # 함수 1 안에 함수 2
        d = (1, 2, 3)
        print('Local a =',a) # 이순신
        print('Local b =',b) # 99
        print('Local c =',c) # [ 1 , 2 , 3 ]
        print('Local d =',d) # ( 1 , 2 , 3 )
        
    
    function2()
    print('Enclosing a =',a) # 이순신
    print('Enclosing b =',b) # 99
    print('Enclosing c =',c) # [ 1 , 2 , 3 ]
    #print('Enclosing d =',d) # 오류
function1()
print('Global a =',a) # 홍길동
print('Global b =',b) # 99
# print('Global c =',c) # 오류 c는 function1 안에 있음
# print('Global d =',d) # 오류 d는 function2() 안에