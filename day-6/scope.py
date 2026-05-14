# scope.py

def calc(r1):
    result = 3.14*r1*r1 # r1 : 반지름
    return result

r = float(input("원의 반지름 입력 : "))
area = calc(r)
print(area)
# print(result)

######
def calc2(r2):
    a = 3.14*rr**2 # r1 : 반지름
    return a

a = 0 # 전역변수
rr = float(input("원의 반지름 입력 : "))
calc2(rr)
print(a)
