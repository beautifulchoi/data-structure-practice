#1 인접행렬 그래프 dfs 구현

vertex = ['A','B','C','D','E','F','G','H']
adjMat=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

def dfs(graph, start, visited=[]): #start는 0을 시작으로 할 예정임 
    if sorted(visited)==vertex:
        return 
    else:
        visited.append(vertex[start])
        print(vertex[start], end=' ') #방문기록 저장, 프린트
        for i in range(len(graph[start])): #해당 정점의 간선관계 파악
            if (vertex[i] not in visited) and graph[start][i]==1: #방문 안했고 인접정점 이어져 있으면
                dfs(graph, i, visited) #그 정점에서 dfs 반복

dfs(adjMat, 0)
    
    
    
    

    
