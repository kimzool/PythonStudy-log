print("sort()와 람다함수")
# 리스트 안에 튜플
students = [
    ("홍길동",60),
    ("권율",92),
    ("이순신",88),
    ("유관순",74)
]

stu_list=sorted(students,key = lambda x : x[1])
print("오름차순")
print(stu_list)
for a in stu_list: #stu_list 요소를 꺼내서 a 변수에 대입
    print(a)

stu_list=list(sorted(students ,key = lambda x : x[1],reverse = true))
# reverse : 역순(거꾸로)
print("내림차순")
print(stu_list)
print("=" * 50)
print("딕셔너리->리스트 의 정렬")

stu=[
    {"name":"윤태원",'score':70},# item이 2개
    {"name":"잘생김",'score':80},
    {"name":"귀여움",'score':95},
    {"name":"나도 알아",'score':52}

]
# "name", "score" : 키
#"유재석", 52 : 값
# 점수 기준으로 내림차순

stu_desc=sorted(stu,
                key = lambda s : s["score"],
                reverse=True)

print("점수가 높은 순서로부터 출력")

for ss in stu_desc:
    print(ss["name"],ss["score"])
