#교집합 함수 구현
"""
작성자: 최용준
작성일:2021.10.18
1. 집합의 교집합 함수를 정렬하여 구현한다. 
2. 실습문제 7.3: 교집합 함수 구현
3. 방법: A와 B를 미리 정렬해놓은 후, 두 집합을 하나씩 비교하여 같은 값들을 새로운 교집합을 만들어 넣는다.
알고리즘:
1. 집합 클래스 가져옴
2. intersect 함수 구현
-A와 B의 값을 인덱스 0 부터 비교
-만약 A의 값이 더 크다면 B의 인덱스 하나 증가,  B의 값이 더 크다면 A의 인덱스 하나 증가
-같은 값을 발견하면 새로만든 교집합에 아이템 삽입
-한 쪽의 길이까지 루프 다 진행되면 종료 
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

    def interset(self,setB):
        i=0 # A의 인덱스
        j=0 # B의 인덱스
        newSet=Set() 
        while(i<len(self.items) and j<len(setB.items)): #A B 둘 중 하나의 길이를 벗어나면 루프탈출
            if self.items[i] < setB.items[j]: #B의 아이템이 더크다면
                i+=1 #A 의 인덱스 하나 증가
            elif self.items[i] > setB.items[j]: #A의 아이템이 더 크다면
                j+=1 # B의 인덱스 하나 증가
            else:
                newSet.items.append(self.items[i]) # 같은 경우 새로운 집합에 아이템 넣고 둘다 인덱스증가
                i+=1; j+=1
        return newSet

            
        return newSet

test1=Set()
test2=Set()

test1.insert(1)
test1.insert(2)
test1.insert(3)
test1.insert(4)
test1.insert(5)

test2.insert(4)
test2.insert(5)
test2.insert(6)
test2.insert(7)
k=test1.intersect(test2)
print(k)

