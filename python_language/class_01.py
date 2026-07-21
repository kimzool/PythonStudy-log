# 클래스와 인스턴스
print("클래스와 인스턴스")
print("="* 60)

class Student:
    s_name = "중앙직업전문학교"

    def __init__(self,name,score): # 자바의 생성자와 유사
        self.name = name
        self.score = score

    def print_info(self):
        print("학교 : ",Student.s_name)
        print("이름 : ",self.name)
        print(" 점수 : ",self.score)

# Student s1 = new Student("홍길동",90)

s1 = Student("홍길동",90) # 객체 1 생성
s2 = Student("유관순",75) # 객체 2 생성

s2.score = 99
s1.print_info()
s2.print_info()

Student.s_name = "글로벌 학교"
print("학교명 : ",Student.s_name)

print("\n"+"="*50)
print("파이썬의 함수 오버로딩")

class Calculator:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a*b*c
    
c1 = Calculator() # 객체 생성
print(c1.add(10,20,30))
print(c1.add(100,200)) # 오류
# 파이썬에서는 같은 이름의 함수 여러번 작성하면
# 마지막 작성한 함수가 앞의 함수를 덮어씀

