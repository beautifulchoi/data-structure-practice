from treeADT import *

def path_length(root):
    if root is None:
        return 1
    else:
        cnt=0
        left=path_length(root.left)
        right=path_length(root.right)
        cnt+=1
        return left+right+cnt

c=TNode("C",None,None)
d=TNode('D',None, None)
f=TNode('F',None, None)

e=TNode("E",None,f)
b=TNode("B",c,d)
root1=TNode("A",b,e)

print(path_length(root1))
