"""
작성자: 최용준
작성일:2021.10.08
1. 링크드 리스트를 응용해본다
2. 실습문제 6.3: 단순연결리스트를 이용하여 큐 클래스 구현
3. 방법: 예제에서 구현한 단순 연결리스트를 이용하여 연결리스트의 맨뒤를 전단 앞(헤드)을 후단으로 사용
알고리즘:
1. 연결리스트 인스턴스 생성
2. 
-
3. 
4. 
5. 
"""

from linkedList import LinkedList

class LinkedQueue:
    def __init__(self):
        self.queue=LinkedList()
    def enqueue(self,item): #후단 삽입
        if self.queue.size()==0: #큐가 비어있으면 아이템 추가
            self.queue.insert(0,item)
        else:
            endIdx=self.queue.size() #큐가 비어있지 않다면 큐의 크기를 통해 마지막 인덱스를 찾음
            self.queue.insert(endIdx,item) #큐의 마지막 인덱스까지 가서 아이템을 넣음

    def dequeue(self): #전단 삭제
        pop=self.queue.head.data #큐의 헤드 데이터를 저장
        self.queue.delete(0) #큐의 맨 앞을 삭제/delete를 구현할 때 맨앞을 삭제하면 헤드 포인터를 이동하게 짜놔서 고려안해도 됨
        return pop #저장했던 데이터(기존 헤드 데이터) 반환 

    def peek(self):
        return self.queue.head.data
    
    def clear(self):
        self.queue.head = None

    def isEmpty(self):
        return self.queue.head == None

    
q1=LinkedQueue()
q1.enqueue('one')
q1.enqueue('two')
q1.enqueue('three')
print(q1.dequeue())
print(q1.dequeue())
print(q1.isEmpty())
print(q1.peek())
print(q1.clear())
print(q1.isEmpty())
q1.enqueue('three')
print(q1.isEmpty())

