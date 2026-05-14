#1~100까지 합과 개수

sum = 0 #합을 저장할 변수
count = 0 #개수를 저장할 변수
i = 1 #반복문에서 사용할 변수
while i <= 100:
    sum += i #sum = sum + i
    count += 1 #count = count + 1
    i += 1 #i = i + 1  
print("1~100까지의 합 :", sum)
print("1~100까지의 개수 :", count)