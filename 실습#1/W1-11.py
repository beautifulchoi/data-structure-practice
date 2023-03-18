#for문(while)의 무한 반복과 break 문을
#  이용하여 0이 입력될 때까지
#  입력 받은 정수 중
#  가장 큰 정수를 출력하는 
# 프로그램을 작성하시오.
arr=[]
while(True):
    n=int(input())
    if n==0:
        break
    arr.append(n)

print(max(arr))