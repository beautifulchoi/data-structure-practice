#플라톤의 국가 파일입출력으로 가져와서 허프만 코드로 파일을 압축하기

"""
1.텍스트 파일 불러와서 알파벳 빈도측정하기(구두점 싹 빼고, 대소문자 구분x)
2.허프만 코드 작성하기
3. 허프만 코드로 파일을 압축하기 -> 파일 크기 비교하기 
4. 압축한 파일 재복원
"""

#1 텍스트 파일 불러와서 알파벳 빈도 측정
def check_freq(filename):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    freqArr=[0]*26 #알파벳의 빈도를 담는 리스트

    file=open(filename, 'rt', encoding='UTF8')
    lines=file.readlines()
    for line in lines:
        for ch in line: 
            #ch가 a~z냐에 따라서 빈도수 배열의 값을 한칸씩 올려야함
            ch=ch.lower()
            if ch in alphabet:
                idx = alphabet.find(ch)
                freqArr[idx] += 1
    alphabetDic={}
    for i in range(len(alphabet)):
        alphabetDic.update(zip(alphabet,freqArr))
    return alphabetDic, freqArr #편의를 위해 알파벳을 빈도와 매핑한 딕셔너리와, 빈도수만 저장한 배열 둘다 리턴

#2. 허프만 코드 작성하기
#허프만 트리 만들기
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

#허프만 트리에 코드를 부여하기
# 왼쪽 자식의 인덱스 = 부모인덱스*2
# 오른쪽 자식 인덱스 =부모 인덱스*2 +1

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
        a=(tree[idx-1],''.join(codenum))
        dict.update(a)
    return dict
            
            
            
            


freq=check_freq('the republic.txt')
print(make_tree(freq))

#가변길이 코드작성





            

        