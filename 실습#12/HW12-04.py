#4 기수정렬 이용하여 10이하의 정수를 정렬하라 

#2개 버킷
#10개 버킷
#16개 버킷 이용

#진수를 변환하는 함수
def trans_digit(n,bucket):
    if bucket==2:
        transnum = int(format(n, 'b'))
    elif bucket==16:
        transnum= format(n, 'x')
    else:
        transnum= n
    return transnum

from queue import Queue                 
def radix_sort(A,buckets,digit) :
    queues = []						    
    for i in range(buckets) :
        queues.append(Queue())			#큐리스트에 큐 인스턴스들(버켓들)을 담음
    n = len(A)
    for idx in range(n):
        newone=trans_digit(A[idx],buckets)
        A[idx]=newone # 아이템들을 새로운 진수로 맞춤 (16진법 구현 아직 못함)

    factor = 1							
    for d in range(digit) :		#자리수별 버켓담기 	
        for i in range(n) :				
            queues[(A[i]//factor) % buckets].put(A[i]) #1의자리부터 순차적으로 버킷에 담음 
        i = 0
        for b in range(buckets) :		#버킷에서 뺴서 정렬하는 과정
            while not queues[b].empty(): #버킷이 비어있지 않다면
                A[i] = queues[b].get()	# 버킷에서 요소 빼내서 리스트에 저장
                i += 1
        factor *= buckets					#다음자리수 이동 
        print("step", d+1, A)			

import random
data = []
for i in range(10) :
    data.append(random.randint(1,99))	
radix_sort(data,10,2)				
print("Radix: ", data)

data = []
for i in range(10) :
    data.append(random.randint(1,99))	
radix_sort(data,2,2)
for idx in range(len(data)):
    data[idx]=int(str(data[idx]),2)
print("Radix: ", data)
