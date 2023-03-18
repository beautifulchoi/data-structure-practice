#4 신장트리 구하는 함수를 깊이 우선탐색으로 구현

vertex = ['A','B','C','D','E','F','G','H']
adjMat=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

""" 1.정점방문
    2.정점의방문기록 추가
    3.정점의 간선들을 연결시킴 
    4.연결되어있는 노드로 이동-> 반복(방문하지 않은 노드에 대해서)""" 

def dfs(graph, vertexIdx=0, visited=[], spantree=[]): #vertexIdx는 0을 시작으로 할 예정임 
    visited.append(vertex[vertexIdx])#방문기록 추가
    for i in range(len(graph[vertexIdx])): #해당 정점의 간선관계 파악
        if (vertex[i] not in visited) and graph[vertexIdx][i]==1: #방문 안했고 인접정점 이어져 있으면
            spantree.append([vertex[vertexIdx], vertex[i]])
            dfs(graph, i, visited,spantree) #그 정점에서 dfs 반복     
    return spantree
    
print(dfs(adjMat))