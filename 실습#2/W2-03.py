#2.13
def bi_coeff(n,k):
    if k==0 or k==n:
        return 1
    elif k>0 and k<n:
        return bi_coeff(n-1,k-1)+bi_coeff(n-1, k)

print(bi_coeff(10,2))        

