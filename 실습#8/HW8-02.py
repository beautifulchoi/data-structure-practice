from treeADT import *
"""
작성자: 최용준
작성일:2021.11.05
1. 트리구조를  파악하고, 재귀를 통해 트리 순회를 이해한다
2. 실습문제 8.2: 완전이진트리 검사
3. 방법: 후위순위법을 이용하여 깊이 탐색을 한 후, 트리의 왼쪽과 오른쪽을 검사한다
4.알고리즘 
1. 후위 순위법을 사용하여 맨 밑단계까지 내려간다
2. 맨 밑에서 트리의 왼쪽은 비었는데 오른쪽이 안비었다면 false를 출력한다

"""
def is_complete_binary_tree(root):
    if root is None:
        return 
    else:
        treeLeft=is_complete_binary_tree(root.left)
        treeRight=is_complete_binary_tree(root.right)
        if (treeLeft==None and treeRight!=None): # 왼쪽의 자식은 없는데 오른쪽 자식은 있다면 false
            return False
        return True

g=TNode('G',None, None)
h=TNode('H',None, None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",g,h)
c=TNode("C",e,f)
b=TNode("B",d,None)
root1=TNode("A",b,c)

print(is_complete_binary_tree(root1))
