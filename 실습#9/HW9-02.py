#clear 
"""
작성자: 최용준
작성일:2021.11.9
1. 이진탐색트리를 이해하고 이를 응용해본다
2. 실습문제 9.2: 이진 탐색 트리의 삽입 연산을 반복구조로 구현하기
3. 구현 방법: 트리를 탐색하여 탐색에 실패하면 그자리가 삽입자리임으로 노드를 추가한다.
4.알고리즘 
-트리의 왼쪽과 오른쪽을 계속 타고 내려가면서 트리를 탐색한다
-만약 노드의 자식이 없다면 그자리가 삽입할 자리임으로 새로운 노드를 자식에 추가한다.
"""
from bstADT import*

    #루트와 해당노드의 키를 계속하여 탐색함
    #만약 루트키보다 노드 키가 작다면 왼쪽으로 가야함
        #-> 이 경우 루트는 n.left 가 됨
    #만약 루트키보다 노드 키가 크다면 오른쪽으로 가야함
        #-> 이 경우 루트는 n.right 가 됨

    #만약 두 경우에서 모두 다음 키가 있어야 하는데 없다면 그자리가 삽입자리임
def insert_bst_iter(r,n):
    findLev=r

    while(n!=None):
        if findLev.key>n.key:
            if findLev.left==None:
                findLev.left=n
                return
            findLev=findLev.left
                
        elif findLev.key<n.key:
            if findLev.right==None:
                findLev.right=n
                return 
            findLev=findLev.right
    return False
    
root=BSTNode(18,1)
t1=BSTNode(7,2)
t2=BSTNode(26,3)
t3=BSTNode(3,4)
t4=BSTNode(12,5)
t5=BSTNode(31,6)
t6=BSTNode(27,7)

insert_bst_iter(root,t1)
insert_bst_iter(root,t2)
insert_bst_iter(root,t3)
insert_bst_iter(root,t4)
insert_bst_iter(root,t5)
insert_bst_iter(root,t6)

node=BSTNode(9,3)
insert_bst_iter(root,node)
print(root)
print("")
        