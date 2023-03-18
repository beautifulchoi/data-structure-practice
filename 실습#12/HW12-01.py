#  1.오름차순 검사하여 정렬되어있으면 True, 아니면 False
#버블정렬 이용
arr1=[1,2,3,4,5,6,7,8]
arr2=[1,2,3,5,7,9,6]

def isUpsorted(A) :					
    n = len(A)
    for i in range(n,0,-1) :		
        for j in range(i-1): 
            if A[j]>A[j+1]: #버블 정렬하면서 앞의 숫자가 뒤의 숫자보다 더 크다면 바로 False 리턴
                return False
    return True #버블 정렬로 탐색하면서 다 지나간다면 True

print(isUpsorted(arr1))
print(isUpsorted(arr2))
