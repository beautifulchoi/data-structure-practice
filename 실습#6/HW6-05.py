from linkedList import LinkedList
from linkedList import Node

class Term:
    def __init__(self,expo,coef):
        self.expo=expo
        self.coef=coef
    
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()
        self.addhead=None

    def read(self):
        a,b=map(int, input().split())
        term=Term(a,b)
        if self.head==None:
            super().insert(1,term)
        else:
            if self.head.data.expo<term.expo: #지수 가장 큰녀석 들어온다면
                super().insert(0,term)#새로 들어온 녀석을 제일 앞으로
            elif self.head.data.expo>term.expo:#지수 더 작은 녀석 들어오면
                    nextNode=self.head.link
                    if nextNode==None:
                        super().insert(1,term)
                    else:
                        while(True):
                            if nextNode.data.expo<term.expo:#다음 노드의 지수가 들어오는 노드의 지수보다 작다면
                                node=Node(term,nextNode)
                                self.head.link=node
                                break
                            elif nextNode.data.expo>term.expo:#다음 노드의 지수가 들어오는 노드의 지수보다 크다면
                                if nextNode.link==None:
                                    nextNode.link=Node(term,None)
                                    break
                                else:
                                    nextNode=nextNode.link
                                
    def display(self, msg='입력 다항식:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print('{} x^{} +'.format(node.data.coef, node.data.expo), end=' ')	
            node = node.link		    
        print()

    def add(self, polyB):
        nodeA=self.head
        nodeB=polyB.head
        
        while(nodeA!=None):
            while(nodeB!=None):
                if nodeA.data.expo==nodeB.data.expo: #A항과 B항의 지수가 같을 경우 
                    newterm=Term(nodeA.data.expo, nodeA.data.coef+nodeB.data.coef)
                    self.head=nodeA.link
                    polyB.head=nodeB.link
                    self.addhead=Node(newterm)

                elif nodeA.link.expo>nodeB.link.expo: #A항의 지수가 더 클경우
                    self.addhead.link=nodeA #다음 노드에 A항 연결
                    self.head=nodeA.link

                elif nodeA.link.expo<nodeB.link.expo: #B항의 지수가 더 클경우
                    self.addhead.link=nodeB #다음 노드에 B항 연결
                    polyB.head=nodeB.link
                
        return self.addhead
test1=SparsePoly()
test2=SparsePoly()
test1.read()
test1.read()
test1.read()
test1.display()

test2.read()
test2.read()
test1.add(test2)
test1.read()
