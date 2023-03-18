#위의 문제를 0을 입력하기 전까지는 
# 계속 수행(인수 출력)하도록 수정하시오.

while(True):
    i=1
    n=int(input())
    if n==0:
        break
    while(i<n):
        if n%i==0:
            print(i, end=' ')
        i+=1
    print("")
    
   