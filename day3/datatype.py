#리스트
subway=["아이유","변우석","박지훈","유재석"]
print(subway)

subway.append("장원영")
print(subway)

subway.insert(1,"카리나")
print (subway)

print(subway.index("박지훈"))  #위치

print(subway.pop()) # 뒤 자료 삭제
print(subway)

name= subway.pop(1) #1번째 삭제된 값을 반환
print(name) 

subway.remove("유재석")
print(subway)

subway.append("아이유")
print(subway)

subway.remove("아이유")
print(subway)

print(subway.count("아이유"))

num_list=[2,4,5,1,3]
print(num_list)

num_list.sort()
print(num_list) #오름차순 정렬 (작 -> 큰)

num_list.reverse()
print(num_list) #내림차순

num_list.clear()
print(num_list)

#튜플 : 순서 있음, 나열형, 변경불갖
menu=("깁밥","오뎅")
print(menu)

# menu[1]="피자" 오류
# print(menu)

(name, age, addr)=("이순신",30,"안산")  
print(name,age,addr)

#딕셔너리 : 키와 값 쌍으로 구성
classroom={407:"개발자과정",402:"영상과정"}
print(classroom)
print(classroom[407])
# print(classroom[404])

print(classroom.get(407)) #값 출력
print(classroom.get(404)) #none

print(classroom.keys()) #키
print(classroom.values())   #값
print(classroom.items())    # 키 : 값

del classroom[402]
#del -> 전반적인 통용되는 삭제
print(classroom)
