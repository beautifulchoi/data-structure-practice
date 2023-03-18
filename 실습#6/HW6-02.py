#2 연결 리스트 클래스의 merge 연산 구현

class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link

class LinkedList:			
    def __init__( self ):			
        self.head = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = None		    

    def size( self ):			
        node = self.head		
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.link		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        node = self.head			     
        while pos > 0 and node != None :
            node = node.link		     
            pos -= 1			         
        return node	

    def getEntry(self, pos) :		    
        node = self.getNode(pos)		
        if node == None : return None	
        else : return node.data		    

    def replace(self, pos, elem) :	    
        node = self.getNode(pos)		
        if node != None: node.data = elem	

    def find(self, data) :		    
        node = self.head
        while node is not None:		
            if node.data == data : return node	
            node = node.link
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)		    
        if before == None :         		    
            self.head = Node(elem, self.head)	
        else :					                
            node = Node(elem, before.link)		
            before.link = node		

    def delete(self, pos) :
        before = self.getNode(pos-1)		
        if before == None :         		
            if self.head is not None :		
                self.head = self.head.link	
        elif before.link != None :		    
            before.link = before.link.link

    def merge(self,listB): #merge 함수 구현
        endIdx=self.size()-1 #마지막 노드의 인덱스 값을 구함
        self.getNode(endIdx).link=listB.head #마지막 인덱스의 노드와 listB의 헤드를 연겷
        listB.head=None #리스트 B의 헤드포인터는 초기화시킴

l1=LinkedList()
l1.insert(1,'hibar')
l1.insert(2,'two')
l2=LinkedList()
l2.insert(1,'하위')
print(l1.head.data)
l1.merge(l2)

print(l1.size())
print(l2.size())