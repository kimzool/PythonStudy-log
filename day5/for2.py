#for i in range(6):
# =>0~5 6번 반복
#dictionary : 키 + 값
snack={
    "새우깡" : 3000,
    "매운새우깡" : 3500,
    "양파링" : 4000}

for i in snack:
    print(i) #키값이 출력
for j in snack.items():
    print(j) #키 + 값이 출력
for k in snack.values():
    print(k) #값이 출력

#리스트
fruit = ["파인애플","참외","배","오렌지","골드키위"]
cart=[]
for i in fruit:
    if len(i) >= 3:
        cart.append(i)
print(cart)