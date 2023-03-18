#체이닝을 이용한 해시맵을 수정하여 선형조사법을 이용한 해시맵을 구현

class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

class HashlinealMap:						
    def __init__( self, M ):
        self.table = [None]*(M+1)
        self.M = M

    def hashFn(self, key) :				
        sum = 0
        for c in key :					
            sum = sum +  ord(c)			
        return sum % self.M

    def insert(self, value) :		
        idx = self.hashFn(value)			
        while(self.table[idx] == None or self.table[idx] == 1):
            if(idx < self.M):
                idx = idx + 1
            elif (idx==self.M):
                idx = 1
        self.table[idx] = Entry(idx, value)

    def search(self, value) :
        idx = self.hashFn(value)
        while(self.table[idx]!=value):
            if(idx<self.M):
                idx = idx+1
            elif(idx==self.M):
                idx = 1
        return self.table[idx]

    def delete(self,value) :
        idx = self.hashFn(value)
        while(self.table[idx]!=value):
            if(idx<self.M):
                idx = idx+1
            elif(idx==self.M):
                idx = 1
        self.table[idx] = 1	
        
    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)) :
            if (self.table[idx] != None and self.table[idx] != 1):
                print(self.table[idx], end='')
d = {}									
d['data'] =  '자료'						
d['structure'] = '구조'
d['sequential search'] = '선형 탐색'
d['game'] = '게임'
d['binary search'] = '이진 탐색'
print("나의 단어장:")
print(d)								

if d.get('game') : print("탐색:game --> ", d['game'])
if d.get('over') : print("탐색:over --> ", d['over'])
if d.get('data') : print("탐색:data --> ", d['data'])

d.pop('game')						
print("나의 단어장:")
print(d)