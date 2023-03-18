import heapq
def make_tree(freq):
    heap=[]
    for n in freq :
        heap.append(n)
    heapq.heapify(heap)
    heapPlus=[]
    for i in range(0, n) :
        e1 = heapq.heappop(heap)
        e2 = heapq.heappop(heap)
        heapq.heappush(heap,e1 + e2)
        heapPlus.append(e1)
        heapPlus.append(e2)
    heapPlus.append(heapPlus[-1]+heapPlus[-2])
    return heapPlus

def giveCode(tree):
    #parent = A[i] 라면 left== A[i*2] , right==A[i*2 +1] 
    #인덱스를 계속 2로 나눠서 나누어떨어진다면 1부여, 아니면 0부여
    dict={}
    for idx in range(len(tree)):
        idx=idx+1
        codenum=[]
        while(idx>1):
            det=item%2 #인덱스를 2로 나눠서 따짐
            if det==0: #나누어 떨어지는수 -> 1
                codenum.append(1)
            else:
                codenum.append(0)
            item=item//2
        codenum.reverse()
        a=(tree[idx-1], ''.join(codenum))
        dict.update(a)
    return dict

freq=[15,12,8,6,4]
print(make_tree(freq))
print(giveCode(make_tree(freq)))
print()