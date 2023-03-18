
#1. 배열에 들어있는 숫자들을 이진탐색트리에 추가 
#2. 트리 중위 순회하며 숫자 출력
"""
작성자: 최용준
작성일:2021.11.9
1. 이진탐색트리를 이해하고 이를 응용해본다
2. 실습문제 9.3:이진탐색트리 중위 순회하여 배열에 들어있는 숫자들을 정렬시키기 
3. 구현 방법: 전위순회를 이용한다.
4.알고리즘 
-배열의 아이템들을 전부 트리 노드로 만들기
    배열의 값들을 인덱스 하나씩 늘리면서 노드를 만들고 그 노드들을 삽입한다.
-트리 호출하면서 배열 정렬시키기
    전에 배웠던 전위순회를 사용하여(재귀구현) 배열을 프린트 한 후, 새로운 배열에 넣는다.
"""

from bstADT import*

def make_arr_toTree(arr):
    idx=1
    root=BSTNode(arr[0],0)
    while(idx<len(arr)):
        node=BSTNode(arr[idx],idx)
        insert_bst(root, node)
        idx+=1
    return root

newarr=[]
def sort_tree(r): 
    if r==None:
        return
    else:
        sort_tree(r.left)
        newarr.append(r.key)
        print(r.key, end=' ')
        sort_tree(r.right)
    
sample=[11,3,4,1,56,5,6,2]
sort_tree(make_arr_toTree(sample))
print("")
print(newarr)

