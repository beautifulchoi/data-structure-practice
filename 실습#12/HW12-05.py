#하이브리드 정렬 알고리즘 구현
"""
32개의 부분리스트로 쪼갬
각각의 부분리스트는 삽입정렬시킴
삽입 정렬이 완료되면 각각의 부분리스트를 병합정렬
"""

def insertion_sort(A) :			#삽입정렬 함수(예제 코드 이용)		
    n = len(A)
    for i in range(1, n) :				
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :		
            A[j + 1] = A[j]				
            j -= 1
        A[j + 1] = key
    return A

#합병정렬 코드
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
count=0#몇번 분할되는지 체크하는 변수(2^n배로 부분리스트 늘어남)
def hybrid_sort(list):
    global count 
    count+=1
    if len(list) <= 1:
        return list
    elif count==4: #분할이 4번 되었으면 다음 분할 후 삽입정렬해야함
        mid = len(list) // 2
        leftList = insertion_sort(list[:mid]) #왼쪽을 선택정렬
        rightList = insertion_sort(list[mid:]) # 오른쪽을 선택정렬 
        return merge(leftList, rightList) #합치기 
        
    else:
        mid = len(list) // 2
        leftList = list[:mid]
        rightList = list[mid:]
        leftList = hybrid_sort(leftList) #왼쪽 쪼갬
        rightList = hybrid_sort(rightList)		#오른쪽 쪼갬
        return merge(leftList, rightList) #합병 
import random
data = []
for i in range(100) :
    data.append(random.randint(1,999))#난수 999개 생성

print(hybrid_sort(data))



        
