#P2.1
payList=[1200,4600,8800,15000]
payPercent=[0.06,0.15,0.24,0.35]
payFor=[]
income=int(input())
for i in range(4):
    payFor.append(payList[i]*payPercent[i])

if income<=1200:
    pay=income*0.06
elif income<=4600:
    pay=payFor[0]+(income-1200)*0.15
elif income<=8800:
    pay=sum(payFor[:2])+(income-4600)*0.24
elif income<=15000:
    pay=sum(payFor[:3])+(income-8800)*0.35
else:
    pay=sum(payFor)+(income-15000)*0.38

print(pay)
