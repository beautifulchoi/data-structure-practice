#차집합 함수 구현 
"""
작성자: 최용준
작성일:2021.10.18
1. 집합의 차집합 함수를 정렬하여 구현한다. 
2. 실습문제 7.4: 차집합 함수 구현
3. 방법: A와 B를 미리 정렬해놓은 후, 값을 처음부터 비교하여 A와 B중 같은 아이템을 A에서 제외시킨다. 
알고리즘:
1. 집합 클래스 가져옴
2. difference 함수 구현
-A와 B의 값을 인덱스 0 부터 비교
-만약 A의 값이 더 크다면 B의 인덱스 하나 증가,  B의 값이 더 크다면 차집합 함수에 A아이템을 넣고 A의 인덱스 하나 증가
-같은 값을 발견하면 A,B 인덱스 둘다 하나씩 증가
-B의 길이가 더 짧을 경우, A의 남은 값들을 차집합 함수에 대입
"""
class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	

    def display(self, msg):		
        print(msg, self.items)	

    def insert(self, elem) :                
        if elem in self.items : return      
        for idx in range(len(self.items)) : 
            if elem < self.items[idx] :     
                self.items.insert(idx, elem)
                return
        self.items.append(elem)             

    def __eq__( self, setB ):       	
        if self.size() != setB.size() :	
            return False
        for idx in range(len(self.items)): 			
            if self.items[idx] != setB.items[idx] :	
                return False
        return True

    def union( self, setB ):        	
        newSet = Set()					
        a = 0							
        b = 0							
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            if valueA < valueB :		
                newSet.items.append( valueA )	
                a += 1					
            elif valueA > valueB :		
                newSet.items.append( valueB )	
                b += 1			
            else : 				
                newSet.items.append( valueA )	
                a += 1					
                b += 1
        while a < len( self.items ):	
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :	
             newSet.items.append( setB.items[b] )
             b += 1
        return newSet	

    def difference(self,setB):
        i=0 # A의 인덱스
        j=0 # B의 인덱스
        newSet=Set() 
        while(i<len(self.items) and j<len(setB.items)): #A B 둘 중 하나의 길이를 벗어나면 루프탈출
            if self.items[i] < setB.items[j]: #B의 아이템이 더크다면
                newSet.items.append(self.items[i]) #A의 아이템을 새로운 집합에 넣음 
                i+=1 #A 의 인덱스 하나 증가
            elif self.items[i] > setB.items[j]: #A의 아이템이 더 크다면
                j+=1 # B의 인덱스 하나 증가
            else:
                i+=1; j+=1
        if i<len(self.items):#B가 더 짧은 경우, A의 남은 원소들 대입
            newSet.items=newSet.items+self.items[i:]
        return newSet



test1=Set()
test2=Set()

test1.insert(1)
test1.insert(3)
test1.insert(5)
test1.insert(7)
test1.insert(9)

test2.insert(2)
test2.insert(3)

k=test1.difference(test2)
print(k)

