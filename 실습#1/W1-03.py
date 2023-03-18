#1부터 100사이의 숫자(정수) 중에서 3의 공배수(3,6,9,12,..)들의 총합을 출력하는 프로그램을 작성하시오.(while문 사용)
i=1
threesArr=[]
sum=0
while(i*3<=100):
    threesArr.append(i*3)
    i+=1
    if i*3>100:
        for k in threesArr:
            sum+=k

print(sum)