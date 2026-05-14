# set(집합)
# 순서가 없음, 중복 안됨
# {}, set([])

my_set={"홍길동","김길동","장길동"}
print(my_set)

football={"홍길동","김길동","장길동"}
#base_ball={"홍길동","오길동","김하성"}
baseball=set={"홍길동","오길동","김하성"}
#교집합
print(football & baseball)
print(football.intersection(baseball))

#합집합
print(football | baseball)
print(football.intersection(baseball))

#차집합
print(football - baseball)
print(football.difference(baseball))

#추가
football.add("김길동") #중복안됨
print(football)

#삭제
baseball.remove("오길동")
print(baseball)

print(type(baseball))

spo1=list(baseball)
print(type(spo1))

spo2=tuple(baseball)
print(type(spo2))

