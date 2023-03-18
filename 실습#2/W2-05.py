#2.15
def reverse(str):
    newList=[]
    for i in range(len(str)):
        newList.append(str[len(str)-i-1])
    result=("".join(newList))
    return result
print(reverse("12345"))