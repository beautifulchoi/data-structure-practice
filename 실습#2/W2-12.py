#P2.5
class Bag:
       def __init__(self):
           bag=[]
           self.bag=bag
       
       def insert(self,item):
              self.bag.append(item)
       
       def remove(self,item):
              self.bag.remove(item)

myBag=Bag()
myBag.insert("휴대폰")
myBag.insert("지갑")
myBag.insert("손수건")
myBag.insert("빗")
myBag.insert("자료구조")
myBag.insert("야구공")
print("내 가방 속 물건: ", myBag.bag)

myBag.insert("빗")
myBag.remove("손수건")
print("내 가방 속 물건: ", myBag.bag)
       

       
              