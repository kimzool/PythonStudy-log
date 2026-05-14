# 상품 이름과 가격 , 수량을 입력받아 총 가격을 출력하세요.
# 상품 이름 : 사과
# 가격 : 1000
# 수랑 : 3
# 출력결과 : 사과의 총 가격은 3000원입니다

name = input("상품 이름을 입력하세요..>>")
price = int(input("가격을 입력하세요..>>"))
quantity = int(input("수량을 입력하세요..>>"))
total_price = price * quantity
print(name + "의 총 가격은 " + str(total_price) + "원입니다.")
# print 안에서 f는 f-string이라 하며 포맷 문자열
# ==>f" {변수 값}
# 숫자 -> 문자로 변환 : str
# 실수는 float만 있음 ( 8바이트 )