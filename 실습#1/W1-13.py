n=int(input())
if n<7:
    print("에러메세지")
else:    
    sum=0
    i=7
    while(i<=n):
        sum+=i
        i+=1
    print(sum)