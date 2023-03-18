#1. 인접리스트에서의 모든 간선 출력함수에서 그래프의 간선들이 중복되어 출력하는거 방지하여 다시 출력함수작성

graphA ={'A' : set([('B',29),('F',10)          ]),
        'B' : set([('A',29),('C',16), ('G',15)]),
        'C' : set([('B',16),('D',12)          ]),
        'D' : set([('C',12),('E',22), ('G',18)]),
        'E' : set([('D',22),('F',27), ('G',25)]),
        'F' : set([('A',10),('E',27)          ]),
        'G' : set([('B',15),('D',18), ('E',25)]) }

def printAllEdge_re(graph):
        vtxSet=set([])
        vtxList=[]
        for vtx in graph:
                vtxList.append(vtx)
                for comp in graph[vtx]: #각 정점의 연결된 간선 집합이 graph[vtx], 집합성분이 comp
                        each=(vtx,comp[0],comp[1]) #(정점, 연결되어있는 다른 정점, 가중치) 튜플 
                        if comp[0] in vtxList:
                                continue
                        vtxSet.add((each)) #정점, 간선, 가중치를 집합에 담음
        print(vtxSet)

printAllEdge_re(graphA)
