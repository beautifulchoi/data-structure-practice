from treeADT import *
"""
작성자: 최용준
작성일:2021.11.05
1. 트리구조를  파악하고, 재귀를 통해 트리 순회를 이해한다
2. 실습문제 8.1: 트리 표현과 순회방법구현
3. 방법: 예제에서 작성한 순회방법을 이용한다
4.알고리즘 
-트리를 만든다
-예제 코드의 4가지 순회방법을 적용한다
-예제코드의 노드 개수와 단말 노드 개수, 트리 높이 함수를 이용한다 

"""
g=TNode('G',None, None)
h=TNode('H',None, None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",g,h)
c=TNode("C",e,f)
b=TNode("B",d,None)
root1=TNode("A",b,c)

preorder(root1)
print("")
inorder(root1)
print("")
postorder(root1)
print("")
levelorder(root1)
print("")
print(count_leaf(root1))
print(count_node(root1))
print(calc_height(root1))
