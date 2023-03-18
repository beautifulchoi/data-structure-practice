#2.12
def sum_reverse(n):
    if n==1:
        return 1/n
    else:
        return 1/n+sum_reverse(n-1)

print(sum_reverse(5))
    
    