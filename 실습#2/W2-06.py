#2.16
def printNum(n):
    if n==0:
        return
    else:
        printNum(n-1)
        print(n, end=' ')
    
def printRevNum(n):
    if n==0:
        return 
    else:
        print(n, end= ' ')
        printRevNum(n-1)

printNum(10)
print('')
printRevNum(10)