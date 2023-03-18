from treeADT import *
"""
작성자: 최용준
작성일:2021.11.05
1. 트리구조를  파악하고, 재귀를 통해 트리 순회를 이해한다
2. 실습문제 8.3: node 레벨 찾기
3. 방법: 
4.알고리즘 
1. 
2. 

"""
def level(root, node):
    
    if root==None:
        return 
    else:
        while(node!=root):
            level(root.left,node)
            level(root.right,node)
            print(root.data)
            return calc_height(root)-calc_height(node)
    return 0

c=TNode("C",None,None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",None,f)
b=TNode("B",c,d)
root1=TNode("A",b,e)

print(level(root1,b))