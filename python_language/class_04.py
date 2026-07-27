print("다중 상속과 mro")
class Login:
    def run (self):
        print("run() 실행")

    def login(self):
        print("login() 실행")

class Printer:
    def run (self):
        print("Printer 클래스 run()실행")

    def print_info(self):
        print("print_info() 실행")

# 다중 상속
class Study(Login,Printer):
    def study(self):
        print("수업중입니다")

s = Study() # 객체 생성
s.login()
s.print_info()
s.study()
s.run() # 상속 우선순위가 높은 메서드가 실행됨.
Printer.run(s) # 상속 우선순위가 낮은 메서드는 직접 그 클래스의 이름을 호출하고 실행해야함.

print("함수 탐색 순서 : ")
print(Study.mro())
# 클래스.mro() : 클래스 찾는 순서를 리스트로 보여줌