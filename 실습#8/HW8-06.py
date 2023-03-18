from treeADT import *
"""
작성자: 최용준
작성일:2021.11.05
1. 트리구조를  파악하고, 재귀를 통해 트리 순회를 이해한다
2. 실습문제 8.6: 이진트리 좌우 반전
3. 방법: 전위 순회법을 이용한다
4.알고리즘 
1. 왼쪽과 오른쪽의 위치를 바꾼다
2. 서브트리들을 호출한다


"""
def reverse(root):
    if root is None:
        return
    else:
        root.left, root.right = root.right, root.left #왼 오 위치변경
        reverse(root.left) 
        reverse(root.right) #전위순회
        
        

c=TNode("C",None,None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",None,f)
b=TNode("B",c,d)
root1=TNode("A",b,e)

reverse(root1)
print(levelorder(root1))