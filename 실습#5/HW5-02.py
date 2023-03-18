#dequeue 구현 다시

from queue import LifoQueue

stack1=LifoQueue()
stack2=LifoQueue()

class NewQueue():
    def __init__(self, st1,st2):
        self.st1=st1
        self.st2=st2
        
    def isEmpty(self):
        if self.st1.empty() and self.st1.empty():
            return 1
        else: return 0

    def clear(self):
        while not self.st1.empty():
            self.st1.get()
        while not self.st2.empty():
            self.st2.get()

    def enqueue(self,item):
        self.st1.put(item)
        if self.st2.empty():
            while not self.st1.empty():
                movedItem=self.st1.get()
                self.st2.put(movedItem)
        
    def dequeue(self):
        if self.st2.empty():
            if not self.st1.empty():
                while not self.st1.empty():
                    movedItem=self.st1.get()
                    self.st2.put(movedItem)
                return self.st2.get()
        else:
            result=self.st2.get() # 스택2에 있는거(맨 앞의 값) 빼냄
            while not self.st1.empty():
                movedItem=self.st1.get() #스택 2가 비었기 때문에 스택1에 남아있는거 가져옴
                self.st2.put(movedItem)
            return result
            
    def peek(self):
        if not self.st2.empty():
            peekItem=self.st2.get()
            self.st2.put(peekItem)
            return peekItem   
        else:
            return
                     

que=NewQueue(stack1,stack2)
que.enqueue("a")
que.enqueue("b")
que.enqueue("c")
print(que.peek())
print(que.dequeue())
print(que.peek())
print(stack2.get())


