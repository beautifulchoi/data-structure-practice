#3 입력 문자열이 영어로 이루어져 있을 때, 카운팅 정렬을 하는 코드 작성

MAX_VAL = 26
def counting_sort(A): 
    output = [0] * MAX_VAL      
    count  = [0] * MAX_VAL      

    for i in A:                 
        count[i] += 1
  
    for i in range(MAX_VAL):    
        count[i] += count[i-1]  
  
    for i in range(len(A)):     
        output[count[A[i]]-1] = A[i] 
        count[A[i]] -= 1

    for i in range(len(A)):     
        A[i] = output[i] 


string=input() #입력을 받음
sortList=[]
for ch in string: 
    ch=ch.lower() #대문자라면 소문자로 내림
    asciinum=ord(ch) #받아온 문자를 아스키코드로 변경 
    sortList.append(asciinum-97) #아스키코드의 시작인 97(a)를 빼고 리스트에 담음
counting_sort(sortList) # 카운팅정렬 
for i in range(len(sortList)):
    sortList[i]=chr(sortList[i]+97) #다시 원상복구 
print(sortList)    
