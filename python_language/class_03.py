print("상속 , super , 오버라이딩 , 다형성")
# 부모 클래스
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, " 직원이 일합니다 ")

    def print_info(self):
        print("이름 : ",self.name)
        print("급여 : ",self.salary,"원")

# 자식클래스
class Developer(Employee): # 상속 하는 방법  class 클래스이름(부모클래스)
    def __init__(self, name, salary,language):
        # 부모 생성자 호출
        super().__init__(name, salary)

        # 자식만 있는 변수
        self.language = language
    # 오버라이딩(재정의) 
    def work(self):
        print(self.name,"개발자가 ",self.language," 프로그램을 작성합니다")
    # 오버라이딩(재정의)
    def print_info(self):
        super().print_info()
        print("사용 가능 언어 : ",self.language)

# 자식 클래스 2
# 선생님
class Teacher(Employee):
    def __init__(self,name,salary,subject):
        # 부모 생성자 호출
        super().__init__(name,salary)

        # 자식만 있는 변수
        self.subject = subject
    # 오버라이딩(재정의)
    def work(self):
        print(self.name," 선생님이 ",self.subject," 과목을 강의합니다")
    # 오버라이딩(재정의)
    def print_info(self):
        super().print_info()
        print("가르치는 과목 : ",self.subject)

# 객체 생성
d = Developer("홍길동",4500000,"파이썬")
t = Teacher("유관순",3000000,"정보능력")

print("개발자 정보")
d.print_info()
print("\n교사 정보")
t.print_info()

# ---------------------
print("\n직원들의 업무")
e_list = [d,t]

for e in e_list:
    e.work()
# 자바 다형성 : 부모타입 - 자식 객체
# 파이썬 다형성 : 객체가 같은 이름의 함수 갖고 있음
# -> 실행할때마다 각각의 서로다른 객체의 함수가 실행
# 개발자는 개발자의 work()
# 교사는 교사의 work()