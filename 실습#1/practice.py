n=100
i=1
intArr=[]
while(i<=100):
    intArr.append(str(i))
    i+=1
str=",".join(intArr)
str=str.replace(",","")

eachCntArr=[]
for num in range(10):
    cnt=0
    for i in range(len(str)):
        if num==int(str[i]):
            cnt+=1
    eachCntArr.append(cnt)

dicOfCnt=dict()
for num in range(10):
    dicOfCnt[num]=eachCntArr[num]

print(dicOfCnt)