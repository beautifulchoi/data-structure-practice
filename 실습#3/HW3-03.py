#3.3 - clear
class Set:
    def __init__(self):
        self.arr=[1,2,'hi',3]
    
    def contains(self,elem):
        checkIdx=0
        while(checkIdx<len(self.arr)):
            if self.arr[checkIdx]==elem:
                return 1
            checkIdx+=1
        return 0

    def delete(self,elem):
        if self.contains(elem):
            self.arr.pop(self.arr.index(elem))
        return self.arr
    
    def insert(self,elem):
        if self.contains(elem)==0:
            self.arr.append(elem)
        return self.arr
    
    def union(self,setB):
        checkIdx=0
        newArr=[]
        while(checkIdx<len(setB)):
            if self.contains(setB[checkIdx])==0:
                newArr.append(setB[checkIdx])
            checkIdx+=1
        return self.arr+newArr

    def intersect(self,setB):
        checkIdx=0
        newArr=[]
        while(checkIdx<len(setB)):
            if self.contains(setB[checkIdx]):
                newArr.append(setB[checkIdx])
            checkIdx+=1
        return newArr
    
    def difference(self,setB):
        intersectSet=self.intersect(setB)
        checkIdx=0
        newArr2=self.arr.copy()
        #굳이 복사안하고 교집합 길이만큼만 루프 돌려서 아이템 인덱스 찾고 반환하는게 좋았음
        while(checkIdx<len(intersectSet)):
            if self.contains(intersectSet[checkIdx])==1:
                newArr2.remove(intersectSet[checkIdx])
            checkIdx+=1 
        return newArr2
        
    def __sub__(self, setB):
        newSet=self.difference(setB)
        return newSet

mySet=Set()
print(mySet.contains(1))
print(mySet.delete('hi'))
print(mySet.insert(4))
print(mySet.union([3,4,5]))
print(mySet.intersect([1,3,4,5,6,8]))
print(mySet.difference([1,3,4,5,6,8]))
print(mySet-[1,3,4,5,6,8])