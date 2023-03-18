dateOfMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
month,day=map(int, input().split())
for i in range(1,13):
    if month==1:
        print(day)
        break
    elif month==i:
        totDate=sum(dateOfMonth[:i-1])+day
        print(totDate)
        break
            

