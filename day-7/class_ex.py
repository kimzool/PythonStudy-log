# class_ex.py

# 부모 클래스
class Passbook:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance


    def deposit(self,money):
        self.balance += money
        print(f"{money}원 입금 완료")
        print(f"{self.owner}님의 현재 잔액은 {self.balance}원 입니다")
    
    # 예) 출금 5000, 잔액 3000 => 잔액부족
    def withdraw(self,money):
        if money <= self.balance: 
            # 잔액이 출금금액보다 크거나 같아야한다.
            self.balance -= money
            print(f"{money}원 출금 완료")
            print(f"{self.owner}님의 현재 잔액은 {self.balance}원 입니다")
        else:
            print("잔액 부족")

    def showInfo(self):
        print("예금주 : ",self.owner)
        print("현재 잔액 : ",self.balance)


# 자식클래스
class MinusPassbook(Passbook): # 상속
    # 재정의(오버라이딩) 

    def withdraw(self,money): # 출금 함수

    # 마이너스 한도 : 잔액이 부족하더라도
    # ( 잔액 - 출금액 ) 결과가 -1,000,000 이상이면 출금이 가능
        minusmoney = -1000000
        if minusmoney <= self.balance:
            self.balance -= money
            print(f"{money}원 출금 완료")
            print(f"현재 잔액은 {self.balance}원 입니다")
    # 예 ) 출금금액이 50000원 잔액 0원 ( -1000000 한도 )
        else:
            print("마이너스 한도 잔액 부족")

# 실행 
# 객체 생성 account1 + 생성자 호출( 예금주,잔액 )
account1 = Passbook("전정우",100000)

# 입금 함수 호출 50,000원
account1.deposit(30000)

# 출금 함수 호출 120,000 출금
account1.withdraw(120000)

# 출금 함수 호출 70,000 출금
account1.withdraw(70000)

# 상세 내역출력
account1.showInfo()

# 마이너스 통장에서 120,000 원 출금을 시도하여 정상 출금 및 잔액이 음수
# 추가로 900,000 원을 더 출금하여 마이너스 한도가 정상 작동하는지 확인

account2 = MinusPassbook("김지후",100000)
account2.showInfo()
account2.withdraw(120000) # 자식클래스 호출
account2.withdraw(9000000)


