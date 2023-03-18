#위의 문제에서 1부터 9사이 이외의 숫자를 
# 사용자가 잘못 입력할 수도 있으니, 이 경우에 잘못된 숫자라는 것을 알려주는 에러 메시지를 출력하고 
# 다시 숫자를 입력 받도록 처리하시오.(입력의 유효성 검사)

while(True):
    n=int(input())
    if n<1 or n>9:   
        print("다시 입력해")
        continue     
    for i in range(1,10):
        print("{0}x{1}={2}".format(i,n,i*n))
    break