# class2.py

class Board:
    def __init__(self,title,writer): # 생성자 ( 객체 생성하면서 초기값을 저장 )
        self.title = title
        self.writer = writer
        self.cnt = 0

    def cntup(self):
        self.cnt +=1

b1 = Board("자바의 정석","홍길동")
b2 = Board("파자마의 정석","전정우")

b1.cntup()
b1.cntup()
b2.cntup()

print(b1.title,b1.writer,b1.cnt)
print(b2.title,b2.writer,b2.cnt)