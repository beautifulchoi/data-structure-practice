#어떤 양의 정수(n)를 입력 받아
# (만약 0이나 음의 정수를 입력하면, 
# 에러 메시지를 띄운 뒤, 
# 다시 입력하도록 처리), 
# 그 수의 2n을 구하는 프로그램을 작성하시오.

while(True):
    n=int(input())    
    if n<=0:
        print("다시 쓰세용")
        continue
    else:
        print(2*n)
        break




