# class1.py
# 클래스

class Board:
    def set_data(self,title, writer):
        self.title = title # 오른쪽 title 은 호출할때 받아온 매개변수
                           # 왼쪽 title은 객체(붕어빵)의 멤버변수
                           # 내 자신(객체) 의미 : self
        self.writer = writer
        self.cnt = 0

    def cntup(self):
        self.cnt +=1

# 게시판 객체 생성
# Board b1 = new Board() 자바
board1 = Board() # 객체변수 = 클래스(매개변수)
board2 = Board()
board1.set_data("자바의 정석","홍길동") # 클래스 함수 호출
board2.set_data("파이썬 정석","이순신") # 클래스 함수 호출

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title,board1.writer,board1.cnt)
print(board2.title,board2.writer,board2.cnt)

board3 = Board()
# board3.cntup() # 오류