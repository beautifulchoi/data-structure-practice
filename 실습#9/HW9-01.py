
"""
작성자: 최용준
작성일:2021.11.9
1. 이진탐색트리를 이해하고 이를 응용해본다
2. 실습문제 9.1: 최대 최소 키 이진트리탐색 재귀로 구현
3. 구현 방법: 재귀를 이용하여 트리의 말단노드까지 내려가서 탐색한다.
(제일 작은 값 트리의 맨 왼쪽, 큰값은 오른쪽에 있음을 이용)
4.알고리즘 
-노드값이 존재한다면 계속해서 다음 단계(큰값은 왼쪽자식, 작은 건 오른쪽 자식)로 재귀호출한다
-만약 말단노드(노드의 자식이 없다면) 노드의 키를 리턴한다.
"""
from bstADT import BSTNode
def search_max_bst_recur(n):
    #말단 조건
    if n==None:
        return None
    elif n.right ==None:
        return n.key
    else:
        return search_max_bst_recur(n.right)

def search_min_bst_recur(n):
    #말단 조건
    if n==None:
        return None
    elif n.left ==None:
        return n.key
    else:
        return search_min_bst_recur(n.left)
root=BSTNode(18,1)
t1=BSTNode(7,2)
t2=BSTNode(26,3)
t3=BSTNode(3,4)
t4=BSTNode(12,5)
t5=BSTNode(31,6)
t6=BSTNode(27,7)
from bstADT import insert_bst
insert_bst(root,t1)
insert_bst(root,t2)
insert_bst(root,t3)
insert_bst(root,t4)
insert_bst(root,t5)
insert_bst(root,t6)

print(search_max_bst_recur(root))
print(search_min_bst_recur(root))