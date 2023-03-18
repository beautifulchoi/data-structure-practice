#3.1 - clear
class ListArr:
    def __init__(self):
        self.arr=[1,2,3,4,5]

    def refine_insert(self,pos,elem):
        self.arr.append(self.arr[-1])
        for i in range(len(self.arr)-1,pos,-1):
            temp=self.arr[i-1]
            self.arr[i-1]=self.arr[i]
            self.arr[i]=temp
        self.arr[pos]=elem
        return self.arr

    def delete(self,pos):
        for i in range(pos,len(self.arr)-1):
            temp=self.arr[i+1]
            self.arr[i+1]=self.arr[i]
            self.arr[i]=temp
        self.arr.pop()
        return self.arr

    def find(self,elem):
        for i in range(len(self.arr)):
            if self.arr[i]==elem:
                return i

    def merge(self,lst):
        self.arr.append(0)
        for i in lst:
            self.refine_insert(len(self.arr)-1,i)
        self.delete(len(self.arr)-1)
        return self.arr
myArr=ListArr()
print(myArr.arr)
print(myArr.refine_insert(1,'hi'))
print(myArr.delete(1))
print(myArr.find(5))
print(myArr.merge([4,5]))