#2.14
def fac(n):
    tot=1
    for i in range(1,n+1):
        tot=tot*i
    return tot

def bino_eff(n,k):
    if k==0 or k==n:
        return 1
    elif k>0 and k<n:
        return fac(n)/(fac(k)*fac(n-k))

print(bino_eff(6,2))