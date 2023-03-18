
class Stack : #스택 클래스 생성(4.2절 예제 인용)
    def __init__( self ):   
        self.top = []       #스택 배열 생성

    def isEmpty( self ): return len(self.top) == 0 #스택이 비었는지 확인(비었으면 1)
    def size( self ): return len(self.top) #스택 사이즈(스택 배열의 크기 반환) 
    def clear( self ): self.top = [] #스택 초기화	

    def push( self, item ): #스택에 아이템 추가
        self.top.append(item)

    def pop( self ): #스택이 비지 않았으면 배열의 마지막에서 빼냄
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek( self ): #스택의 제일 윗부분 반환
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ): #스택에 들어있는거 위에부터 호출
        return "".join(self.top[::-1])

