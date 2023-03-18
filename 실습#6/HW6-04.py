#4 연결리스트를 이중연결리스트로 다시구현

class DNode:			
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem 
        self.prev = prev
        self.next = next

#link를 next로 싹다 바꿈
class LinkedList:			
    def __init__( self ):			
        self.head = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = None		    

    def size( self ):	
        node = self.head		
        count = 0
        while not node == None :
            node = node.next	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.next		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        node = self.head	     
        while pos > 0 and node != None :
            node = node.next		     
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
            node = node.next
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)		    #이전 노드의 주소를 저장 
        if before == None :         		    #맨 앞 노드라면
            self.head = DNode(elem, before, self.head)	#노드를 추가하고 헤드로 설정
        else :					                
            node = DNode(elem, before,before.next)		#이전 노드의 주소를 prev에 저장, 이전주소의 다음 노드를 next에 저장
            before.next = node		#이전 노드의 next 링크에 노드의 주소값 저장
            if before.next.next!=None: #워낙 마지막 노드가 없었더라면(노드가 하나만 있었다면)
                before.next.next.prev=node #pos 다음 노드의 prev를 node 에 연결

    def delete(self, pos) :
        before = self.getNode(pos-1)
        after = self.getNode(pos+1)		
        if before == None :         		
            if self.head is not None :		
                self.head = self.head.next
                self.head.prev=None	
        else:		    
            if after==None:
                before.next=None
            else:
                before.next = before.next.next
                if before.next.next!=None:
                    before.next.next.prev=before
            
l1=LinkedList()
l1.insert(0,'one')
l1.insert(1,'two')
l1.insert(2,'three')
l1.insert(1,'twoplus')
l1.delete(2)
l1.display()	
