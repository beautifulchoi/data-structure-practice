#1. ArrayList 의 sort 연산 구현
"""
작성자: 최용준
작성일:2021.10.18
1. 여러가지 기본 정렬기법을 응용한다
2. 실습문제 7.1: 연 
3. 방법: 3장에서 썼던 ArrayList 클래스를 가져와서 새로운 리스트 클래스에 상속한 후, 삽입정렬을 사용하여 리스트를 정렬한다
알고리즘:
1. 구현된 리스트 클래스 상속
2. 정렬해주는 함수인 sort 를 정의
-키 값을 인덱스 1부터 시작하여 리스트의 마지막 인덱스까지 루프를 돌린다
-각 인덱스의 value 와 key index의 왼쪽부터 차례대로 값을 비교하여 키의 왼쪽에 더 작은 값이 나타나면, 
한칸씩 오른쪽으로 밀고 그자리에 들어간다.
"""
from arraylist import ArrayList

class NewArrayList(ArrayList): #기존에 만들었던 리스트 클래스 상속
    def __init__(self):
        super().__init__() 

    def sort(self):
        length=self.size() 
        
        for idx in range(1,length): #인덱스 1부터 시작하여 비교
            idxKey=self.items[idx] #인덱스의 값
            inidx=idx-1 #내부루프 인덱스 (설정한 인덱스의 왼쪽 값들의 인덱스)
            while(inidx>=0 and idxKey<self.items[inidx]): #내부인덱스가 인덱스-1~ 처음 값 까지/인덱스 키값보다 더 작은 값 만날 때 까지(자리 찾기)
                self.items[inidx+1]=self.items[inidx] #왼쪽 값들을 전부 한칸 씩 이동시킴(인덱스키 값이 들어갈 자리 만들어주기 위해)
                inidx-=1 # 인덱스 1씩 줄여가며 맨 처음값 까지 비교 (중간에 작은 값 만나면 탈출)
            self.items[inidx+1]=idxKey #인덱스 키값이 자기 자리를 찾아 들어감

test1=NewArrayList()
test1.items.append(5)
test1.items.append(3)
test1.items.append(8)
test1.items.append(10)
test1.items.append(1)
test1.sort()
test1.display()