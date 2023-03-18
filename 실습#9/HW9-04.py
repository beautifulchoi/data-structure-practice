#이진 탐색트리를 이용하여 우선순위 큐를 구현하기 
from bstADT import*

"""
작성자: 최용준
작성일:2021.11.9
1. 이진탐색트리를 이해하고 이를 응용해본다
2. 실습문제 9.4: 이진 탐색트리를 이용하여 우선순위 큐를 구현하기 
3. 구현 방법: 예제에서 만들어 놓은 이진탐색트리 함수들을 이용한다
"""
"""
우선순위큐 ADT
priorityQueue() 비어있는 우선순위큐 생성
isEmpty() 우선순위 큐가 공백인지 검사
enqueue(e) 우선순위 가진 항목 e 추가
dequeue() 가장 우선순위가 높은 항목 반환
peek() 우선순위가 높은 요소를 반환
size() 우선순위 큐 항목갯수 반환
clear() 우선순위 큐를 공백상태로 만든다
"""

class PriorityQueue:
    def __init__(self):
        self.root=None

    def isEmpty(self):
        return self.root==None
    
    def clear(self):
        self.root=None

    def size(self):
        return count_node(self.root)

    def enqueue(self, node):
        #새로 들어오는 노드를 삽입함
        insert_bst(self.root, node)
    
    def peek(self):
        #제일 우선순위가 큰 노드를 찾아감
        maxNode=search_max_bst(self.root)
        return maxNode.value

    def dequeue(self):
        #제일 우선순위가 큰 노드를 찾아감
        #우선순위 큰 노드 삭제 시키고 반환
        maxNode=search_max_bst(self.root)
        delete_bst(self.root, maxNode.key)
        return maxNode.value
    