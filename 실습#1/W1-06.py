#0이 입력될 때까지 계속 정수를 입력 받고, 
# 입력된 모든 숫자들의 총합을 출력하시오.
sum=0
while(True):
    n=int(input())
    sum+=n
    if n==0:
        break
print(sum)