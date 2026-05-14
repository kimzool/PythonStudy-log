# Str = input('영어 1글자 입력하세요 : ')

# if Str.isupper():   # 대문자면
#     print(Str.lower())
# else:               # 소문자면
#     print(Str.upper())


    #점수 구간에 해당하는 학점이 아래와 같이 정의 되어 있다.
    #사용자로부터 score를 입력받아 합력을 출력해라.
score = int(input("학점을 입력하세요 : "))
if 81 <= score <= 100:
    print("A")
elif 61 <= score <= 80:
    print("B")
elif 41 <= score <= 60:
    print("C")
elif 21 <= score <=40:
    print("D")
else:
    print("E")