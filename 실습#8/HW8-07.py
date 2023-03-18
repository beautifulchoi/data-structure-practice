
"""
작성자: 최용준
작성일:2021.11.9
1. 힙 트리를 이해하고 이를 응용해본다
2. 실습문제 8.7: 완전이진트리 A가 힙 조건 만족하는지 재귀적으로 검사하기
3. 방법: parent = A[i] 라면 left== A[i*2] , right==A[i*2 +1] 임을 이용한다
4.알고리즘 
-부모 인덱스를 id라고 한다면, 왼쪽 인덱스를 id*2 오른쪽을 id*2+1이라고 지정한다
-루트부터 시작해서 부모의 크기가 왼,오 자식들보다 크다면 전위 순회를 한다.
-만약 오른쪽 자식 인덱스가 마지막 트리배열의 인덱스보다 커진다면 순회를 종료하고 True를 리턴한다
-도중에 힙조건을 만족하지 못한다면 False를 리턴한다. 
"""

#parent = A[i] 라면 left== A[i*2] , right==A[i*2 +1] 
def isMaxHeapRecur(A,id):
    if id*2 >len(A)-2:
        return
    else:
        parentIdx=id
        leftIdx=id*2
        rightIdx=id*2 +1 #부모 왼자식 오른자식 관계

        if (A[parentIdx]>=A[leftIdx]) and (A[parentIdx]>=A[rightIdx]): # 힙조건 만족
            isMaxHeapRecur(A,leftIdx)
            isMaxHeapRecur(A,rightIdx)
            return True
        else:
            return False

def isMinHeapRecur(A,id):
    if id*2 >len(A)-1:
        return
    else:
        parentIdx=id
        leftIdx=id*2
        rightIdx=id*2 +1 #부모 왼자식 오른자식 관계

        if (A[parentIdx]<=A[leftIdx]) and (A[parentIdx]<=A[rightIdx]): # 힙조건 만족
            isMinHeapRecur(A,leftIdx)
            isMinHeapRecur(A,rightIdx)
            return True
        else:
            return False

arr1=[0,1,2,5,3,9,8,6,4,7]
arr2=[0,9,7,6,5,4,3,2,1]

print(isMinHeapRecur(arr1,1))
print(isMaxHeapRecur(arr1,1))
print(isMinHeapRecur(arr2,1))
print(isMaxHeapRecur(arr2,1))

