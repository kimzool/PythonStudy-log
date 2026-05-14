# a = "봄"
# b = "여름" 
# print(a,b, sep= "과",end=" 끝 ")
# sep : 변수 사이에 들어가는 것을 나타낸다
# end : 줄을 바꾸지 않고 옆으로 표시(공백도 가능)

#for i in range(1,100,2) 1~99 2씩증가
#구구단에서 원하는 단을 받아서 출력

# num1=int(input("단을 입력하세요"))
# for i in range(1,10):
#     result = num1 * i
#     print(num1,"X",i,"=",result)

# for dan in range(1,10):
#     print(dan,"단")
#     for i in range(1,10):
#         result = dan * i
#         print(dan,"*",i,"=",result,end = "")
#         print()
import time
print()
for k in range(10,0,-1):
    print(k)
    time.sleep(1)
print("발사!!")