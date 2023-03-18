#P2.3
print("피라미드의 높이를 입력하세요: ", end=' ')
height=int(input())
for level in range(1,height+1):
    levelArr=[]
    for num in range(1,level+1):
           levelArr.append(str(2*num-1))
    levelArr=levelArr+list(reversed(levelArr))
    levelArr.pop(level)
    levelStr= " ".join(levelArr)
    print(levelStr.center(100))