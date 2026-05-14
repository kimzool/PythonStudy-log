

import gugu_modul

while(1):
    num=int(input("메뉴 선택(1: 세로 구구단, 2: 가로 구구단): "))
    if num==1:
        gugu_modul.v_gugudan()
        continue
    elif num==2:
        gugu_modul.h_gugudan()
    elif num==0:
        print("종료")
        break
    else:
        print("다시 입력")