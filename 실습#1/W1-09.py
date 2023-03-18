#10. 소수(prime-number) 검사와 흡사하게 
# 사용자가 입력한 수의 
# 인수들을 모두 출력하는 프로그램을 
# 작성하시오. 8 => 2 4, 12 => 2 3 4 6
i=1
n=int(input())
while(i<n):
    if n%i==0:
        print(i, end=' ')
    i+=1
    