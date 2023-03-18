#2 병합정렬을 반복으로 다시 구현

def merge_sort(A):
    i=2
    while(True):
        for j in range(0,len(A)-1,i):
            w=j-i
            while(w<j and w>0):
                k=w
                while(k>0 and k>j-i and A[k]<A[k-1]):
                    A[k],A[k+1]=A[k+1],A[k]
                    k=k-1
                w+=1
        if (i*2>len(A)):
            for i in range(len(A)):
                k=i
                while (k>0 and A[k]<A[k-1]):
                    A[k],A[k-1]=A[k-1],A[k]
                    k=-1
            break
        i*=2


arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

merge_sort(arr) 
print ("MergeSort: ", arr) 