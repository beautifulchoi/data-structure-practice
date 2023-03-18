#2.17
cnt=0
fiboPerArr=[]
def fibo(n):
    global cnt
    global fiboPerArr
    cnt+=1
   
    fiboPerArr.append(n)
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input())
fibo(n)
print("총:",cnt)
for i in range(n,-1,-1):
    result=fiboPerArr.count(i)
    print("Fibo({0})={1}번".format(i,result))