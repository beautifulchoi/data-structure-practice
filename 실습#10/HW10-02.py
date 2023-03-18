#2 인접행렬 이용하여 BFS 구현( 큐모듈 사용)

from queue import Queue
vertex = ['A','B','C','D','E','F','G','H']
adjMat=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

def bfs(graph, start):
    visited =set([])
    queue=Queue() #큐 객체 생성
    queue.put(start) #큐 객체에 시작점인 A를 넣음(인덱스로 컨트롤)
    while not queue.empty(): #큐에 아무것도 없으면 종료
        idx=queue.get() #deque 
        print(vertex[idx], end=' ') 
        visited.add(vertex[idx]) #방문기록 저장
        for i in range(len(graph[idx])):
            if (vertex[i] not in visited) and (graph[idx][i]==1):
                if i not in queue.queue:
                    queue.put(i)

bfs(adjMat,0)
        
        



    