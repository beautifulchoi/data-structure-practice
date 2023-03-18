from treeADT import *
"""
작성자: 최용준
작성일:2021.11.05
1. 트리구조를  파악하고, 재귀를 통해 트리 순회를 이해한다
2. 실습문제 8.4 이진트리 균형검사
3. 방법: 깊이탐색으로 맨 밑까지 내려간 후, 예제에서 봤던 높이함수를 응용한다
4.알고리즘 
1. 깊이탐색을 한다
2. 트리의 왼쪽 높이와 오른쪽 높이 차이가 1이 넘으면 false를 호출한다

"""
def is_balanced(root):
    if root is None:
        return
    else:
        is_balanced(root.left) 
        is_balanced(root.right)
        if (calc_height(root.left)-calc_height(root.right)>1) or (calc_height(root.right)-calc_height(root.left)>1):
            return False #왼쪽과 오른 쪽 서브트리의 크기차이가 1이넘으면 false
        return True






g=TNode('G',None, None)
h=TNode('H',None, None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",g,h)
c=TNode("C",e,f)
b=TNode("B",d,None)
root1=TNode("A",b,c)

print(is_balanced(root1))
