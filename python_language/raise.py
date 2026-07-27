# raise.py

# raise : 오류를 일부러 발생

age = -5
if age <= 0:
    raise ValueError("나이가 0보다 작거나 같을수는 없다")
print("나이는 : ",age)

try:
    age = int(input("나이를 입력하세요..>>"))

except ValueError as e:
    print("오류발생",e)
else:
    print("나이는 : ",age)
finally:
    print("실행 끝") 
