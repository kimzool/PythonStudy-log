from functools import reduce 

print("reduce 함수 와 람다함수")

# reduce()는 앞에서부터 두 값을 계산하고,
# 그 결과를 다음 값과 다시 계산함

number=[1,2,3,4,5]

reduce(lambda a,b : a+b, number)

sum = reduce(lambda a,b : a+b, number)
print("결과는 :", sum)
