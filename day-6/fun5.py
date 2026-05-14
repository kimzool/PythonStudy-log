# 함수의 " 가변 매개변수 "
# *args : "arguments"의 약자로 , 위치 인자들을 함수로 전달할 때 
# 사용됩니다. ( 튜플 )
# **kwargs : "keyword arguments"의 약자로,
# 키워드 인자들을 함수로 전달할 때 사용됩니다. ( 딕셔너리 )

def manyParam(*args):
    # 몇개의 매개변수를 받을 지 모를때는 변수 앞에 '*'를 붙여준다.
    print(type(args)) # *튜플(tuple)로 저장
    sum = 0
    for i in args:
        sum+=i
    return sum

print(manyParam(1,2,3,4,5,6,7,8,9,10)) # 55
print(manyParam(1,2,3,4,5)) # 15
print('-'*30)

def dictParam(**kwargs):
# **kwargs는 여러개의 매개변수를 받으며 딕셔너리 형태로 함수 내부에 전달
    print(kwargs)

dictParam(a = 'A') # {'a':'A'}
dictParam(x = 10,y = 20,z = 30) # {'x': 10,'y' : 20,'z':30}
print('-'*30)
# 이름이 있는 여러개의 값을 받을 때 사용하는 문법