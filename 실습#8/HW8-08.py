
"""
작성자: 최용준
작성일:2021.11.9
1. 힙 트리를 이해하고 이를 응용해본다
2. 실습문제 8.8: 완전이진트리가 힙 조건 만족하는지 구현하기(반복적으로 )
3. 방법: 자식 = A[lev] 라면, 부모= A[lev//2] 임을 이용한다
4.알고리즘 
-인덱스 시작을 2부터(맨 첫단계)한다.
-자식과 부모의 크기를 비교하여 부모가 더 크다면 인덱스에 2를 곱하여 다음 레벨로 간다.(아래층 비교)
-인덱스 마지막까지 도달하면 True를 리턴한다.
-도중에 조건을 만족하지 못하면 False를 리턴한다.
"""
def isMaxHeapIter(A):
    #자식 = A[lev] 라면, 부모= A[lev//2] 
    startIdxOfLev=2
    while(startIdxOfLev<len(A)):
        for sonIdx in range(startIdxOfLev,2*startIdxOfLev):
            if sonIdx==len(A):
                return True #마지막 인덱스에 도달하면 반복문 탈출                
            if A[sonIdx]>A[sonIdx//2]: #부모보다 자식이 더 크다면 
                return False #false 호출(최대 힙 조건 만족 x)
        startIdxOfLev*=2 #다음 레벨로 이동
    return True

def isMinHeapIter(A):
    #자식 = A[lev] 라면, 부모= A[lev//2] 
    startIdxOfLev=2
    while(startIdxOfLev<len(A)):
        for sonIdx in range(startIdxOfLev,2*startIdxOfLev):
            if sonIdx==len(A):
                return True #마지막 인덱스에 도달하면 반복문 탈출                
            if A[sonIdx]<A[sonIdx//2]: #부모보다 자식이 더 작다면 
                return False #false 호출(최대 힙 조건 만족 x)
        startIdxOfLev*=2 #다음 레벨로 이동
    return True
arr1=[0,1,2,5,3,9,8,6,4,7]
arr2=[0,9,7,6,5,4,3,2,1]

print(isMinHeapIter(arr1))
print(isMaxHeapIter(arr1))
print(isMinHeapIter(arr2))
print(isMaxHeapIter(arr2))
