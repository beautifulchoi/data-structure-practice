# 너비탐색을 이용하여 정점 연결성분 조사 구현
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
#1. 정점방문
#2. 정점방문기록 표시
#3. 정점을 하나의 컬러에 담기
#4. 큐에 인접 노드 담기

#5. 큐에 담긴 노드 꺼내서 일단 중복노드인지 확인-> 반복
def find_connected_component(graph):
    visited=set()
    colorList=[]
    for vtxIdx in range(len(graph)):
        if vertex[vtxIdx] not in visited:
            color=bfs_cc(graph, [], vtxIdx,visited)
            colorList.append(color)
    print("그래프 연결성분 개수= {}".format(len(colorList)))
    print(colorList)

def bfs_cc(graph,color,vertexIdx,visited):
    queue=Queue() #큐 객체 생성
    queue.put(vertexIdx) #큐 객체에 시작점인 A를 넣음(인덱스로 컨트롤)
    while not queue.empty(): #큐에 아무것도 없으면 종료
        idx=queue.get() #deque 
        visited.add(vertex[idx]) #방문기록 저장
        color.append(vertex[idx]) #칼라에 저장
        for i in range(len(graph[idx])):
            if (vertex[i] not in visited) and (graph[idx][i]==1): #방문 안한 정점 중에 연결된 거 발견하면
                if i not in queue.queue: #큐에 중복으로 들어가는거 방지
                    queue.put(i)#enque
    return color

find_connected_component(adjMat)