def v_gugudan():
    for i in range(2,10):
        print(i,"단")
        for j in range(1,10):
            print(i,"*",j,"=",i*j)

def h_gugudan():
    for i in range(2,10):
        print('\n',i,"단")
        for j in range(1,10):
            print("%d * %d = %d " %(i,j,i*j),end=' ')