#2. 연결리스트에 정렬연산 추가(삽입 정렬 구현)
"""
작성자: 최용준
작성일:2021.10.18
1. 연결 리스트를 활용하여 리스트의 정렬을 구현한다.
2. 실습문제 7.2: 연결리스트에 정렬연산 추가(삽입 정렬 구현)
3. 방법: 앞절에서 만들어 놓은 연결리스트 클래스를 온 후, 각 노드에 대해 삽입정렬 구현을 한다  
알고리즘:
1. 구현된 연결 리스트 호출, 상속
2. 노드값의 data들에 대해 삽입정렬 구현
-키 값을 인덱스 1부터 시작하여 리스트의 마지막 인덱스까지 루프를 돌린다
-각 인덱스의 value 와 key index의 왼쪽부터 차례대로 값을 비교하여 키의 왼쪽에 더 작은 값이 나타나면, 
한칸씩 오른쪽으로 밀고 그자리에 들어간다.
"""
from linkedList import LinkedList

class NewLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def sort(self):
        length=super().size()#인덱스를 가져와야함
        for i in range(1,length): # i와 idx의 인덱스 같게 설정해야함
            idx=super().getNode(i) #인덱스 헤드 다음 노드부터 시작 
            before=super().getNode(i-1)
            compareNode=self.head #왼쪽 정렬된 배열에서 인덱스와 비교할 때 비교대상 헤드로 초기화
            for j in range(i): #왼쪽 정렬된 것들과 비교(헤드부터 시작)
                if compareNode.data>idx.data: #만약 인덱스수가 비교하는 수보다 크다면
                    before.link=idx.link #인덱스 수 이전 노드를 비교수 다음 노드로 연결 
                    idx.link=compareNode #인덱스 수가 비교하고 있는 수 앞으로 가서 링크 연결
                    if j>0: #비교하고 있는 수가 헤드가 아니라면
                        super().getNode(j-1).link=idx #비교하고 있는 수의 이전 노드를 인덱스 수와 연결
                    if compareNode==self.head:#비교하고 있는 수가 맨 앞에 있는 수였다면 
                        self.head=idx #인덱스 수를 헤드로 지정
                    break #정렬완료, 다음 인덱스로 넘어감
                elif compareNode.data<idx.data: #인덱스 수가 비교하는 수보다 작다면
                    compareNode=compareNode.link#헤드 다음 노드로 이동

test1=NewLinkedList()
test1.insert(0,5)
test1.insert(1,3)
test1.insert(2,8)    
test1.insert(3,10)
test1.insert(4,1)

test1.sort()
test1.display()