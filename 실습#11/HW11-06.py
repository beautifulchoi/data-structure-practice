#다익스트라 알고리즘을 수정하여 각 경로의 길이와 경로를 출력하는 프로그램 구현

INF = 9999
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' 	]
weight = [ [0,	    7,		INF,		INF,		3,      10,		INF	],
           [7,		0,	    4,		10,	    2,	    6,	    INF	],
           [INF,	4,		0,		2,		INF,		INF,		INF	],
           [INF,	10,		2,		0,      11,		9,		4   ],
           [3,	    2,	    INF,   	11,		0,      13,		5   ],
           [10,	6,	    INF,		9,      13,		0,		INF	],
           [INF,   INF,		INF,   	4,		5,		INF,		0   ] ]    

def choose_vertex(dist, found) :	#최소 거리에 있는 정점 찾는 함수
    min = INF 
    minpos = -1 # 초기값 임의 설정
    for i in range(len(dist)) :	 			
        if dist[i]<min and found[i]==False: #아직 선택 안된 정점이며, 이전에 기록된 거리보다 짧다면
            min = dist[i] #최소 거리 갱신
            minpos = i #정점 갱신
    return minpos #정점의 인덱스를 반환			

def shortest_path_dijkstra(vtx, adj, start) : #다익스트라 알고리즘
    vsize = len(vtx)						#정점 갯수
    dist = list(adj[start])					#최소 거리를 담는 리스트
    path = [start] * vsize					#경로를 담는 리스트 (스타트 지점 A(0))
    found= [False] * vsize					#해당 정점의 인덱스가 아직 선택 안되었으면 False 담는 함수(선택되었으면 True)
    found[start] = True						#시작 정점(A)는 True 로 변환(초깃값)
    dist[start] = 0							#시작 정점(A)거리는 자기자신이므로 0으로 초기화

    for i in range(vsize) :
        u = choose_vertex(dist, found)		#현재 찾아진 지점 부터의 최소 거리 정점을 받아옴
        found[u] = True						#받아온 최소거리 정점을 선택됬다고 표시 

        for w in range(vsize) :			#정점을 추가했기 때문에 선택 안된 정점들에 대하여 거리 갱신
            if not found[w] :				#선택이 안되었다면
                if dist[u] + adj[u][w] < dist[w] :	#현재 기록된 최소거리 값과 추가된 정점을 타고 가는 거리를 비교
                    dist[w] = dist[u] + adj[u][w]	#최소거리 갱신
                    path[w] = u						#이전 정점 갱신 

    return path,dist							            #이전 정점을 반환


print("다익스트라 알고리즘 변경(경로와 길이 같이 출력)")
start = 0		
path = shortest_path_dijkstra(vertex, weight, start)[0]
dist =shortest_path_dijkstra(vertex, weight, start)[1]
wayList=[]
for vtx in range(1,len(vertex)) :
        end=vtx
        print("최단 경로 A->{}: ".format(vertex[vtx]), end=' ')
        while(vtx!=0):
            wayList.append(vertex[path[vtx]])
            vtx=path[vtx]
        wayList.reverse()
        wayList.append(vertex[end])
        for way in wayList:
            print(way, end=' ')
        print("길이:",dist[end])
        print()
        wayList=[]
