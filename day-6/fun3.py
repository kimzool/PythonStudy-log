# fun3.py
def dis_price(price, discount_rate):
    # 할인금액을 먼저 구함
    discount_amount = price * (discount_rate / 100)
    # 가격 - 할인금액 - > 최종금액
    final_price = price - discount_amount
    # 최종 금액 반환
    return final_price




# a 상품 가격 : 10000원 할인율 : 10
price_a = dis_price(10000, 10)  # dis_price 함수명
print(f"a 상품은 {price_a}원 입니다.")  # 할인 금액을 뺀 금액 출력
        

# b 상품 가격 : 50000원 할인율 : 20
price_b = dis_price(50000, 20)  # dis_price 함수명
print(f"b 상품은 {price_b}원 입니다.")  # 할인금액을 뺀 금액 출력   