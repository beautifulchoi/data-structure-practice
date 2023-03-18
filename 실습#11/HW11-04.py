#Prim 알고리즘을 이용하여 가중치 합 구하기

INF = 9999 
def getMinVertex(dist, selected) : # 최소 가중치 정점 반환
    minv = 0	
    mindist = INF
    for v in range(len(dist)) :	  
        if not selected[v] and dist[v]<mindist : #선택 안되었고,현재 최소치보다 작다면(노드와 인접한 정점들이 dist값 갱신됨)
            mindist = dist[v]	     
            minv = v			#최소 정점 갱신		
    return minv, mindist

def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize			
    selected = [False] * vsize		
    dist[0] = 0					    
    vertexList=[]
    weightList=[]
    for i in range(vsize) :			
        u,weight = getMinVertex(dist, selected) # 선택 안된 녀석들 중 최소 정점 받아옴(처음엔A, 다음 부터는 인접정점 중 최소)
        selected[u] = True			#이 정점 선택된 걸로 갱신
        vertexList.append(u)
        weightList.append(weight)
        #print(vertex[u],weight,"->", end=' ')	
        
        for v in range(vsize) :		
            if (adj[u][v] != None):	#만약 연결이 되어있다면
                if selected[v]==False and adj[u][v]< dist[v] : #만약 선택아직 안 된 정점이고 전에 거리계산한 값 보다 거리가 인접정점 거리가 작다면
                    dist[v] = adj[u][v] #거리 갱신

    for i in range(len(vertexList)):
        print("{}".format(vertex[vertexList[i]])+"->",end='')
    print()
    for i in range(len(vertexList)):
        print("{}".format(weightList[i])+" ", end='')

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)

