import random

def get_lotto():
    numbers = [] # 비어있는 리스트
    while  len(numbers) < 6: #6자리까지 반복
        num = input("로또 번호를 입력하세요: ")
        n=random.randint(1,45) # 무작위 수 발생 (1~45) 사이
        #random(모듈): 랜덤 관련 기능을 모아둔 라이브러리 ,randint(함수): 랜덤한 정수 발생
    
        if n not in numbers: # 포함하지 않냐
            # 중복 체크
            numbers.append(n) #6개의 숫자가 있는 리스트에 랜덤한 숫자 추가
    return numbers
print(f"로또번호는 {get_lotto()}입니다")