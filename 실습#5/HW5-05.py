"""
작성자: 최용준
작성일:2021.10.04
1. 덱을 활용하는 방법에 대해 실습한다
2. 실습문제 5.5: 정렬된 배열을 이용한 우선순위 큐 구현 
3. 방법: 리스트를 정렬시키기 위해 sort 함수와 람다식을 활용
알고리즘:
1. enqueue시 값과 우선순위를 튜플로 리스트에 담고 sort 함수를 이용하여 우선순위가 높은 순 정렬
2. dequeue 시 정렬을 이미 해놨으므로 맨 뒤값 뺴내면 됨
"""

class PriorityQueue():
    def __init__(self):
        self.items=[] #아이템 리스트 생성
    
    def isEmpty(self):
        if len(self.items)==0:
            return 1
        else: return 0 #리스트 비어있으면 0반환 
    
    def enqueue(self,item,n):
        self.items.append((item,n))
        self.items.sort(key=lambda x:x[1], reverse=True) #아이템과 우선순위를 튜플형식으로 담음

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()[0] # 맨뒤의 값 뺴냄
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1][0]  #아이템의 데이터값만 반환 
    
    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]
        
que=PriorityQueue()
que.enqueue('a',2)
que.enqueue('b',1)
que.enqueue('c',4)
que.enqueue('d',3)

print(que.items)
print(que.dequeue())
print(que.dequeue())
print(que.peek())
print(que.isEmpty())
print(que.size())