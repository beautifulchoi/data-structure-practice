#Kruskal 최소비용 신장트리 코드 수정해서 MST 가중치 합 출력하기

parent = []     				
set_size = 0    				

def init_set(nSets) :			
    global set_size, parent 	
    set_size = nSets;			
    for i in range(nSets):		
        parent.append(-1)		

def find(id) :					
    while (parent[id] >= 0) :	
        id = parent[id]			
    return id;					

def union(s1, s2) :				
    global set_size				
    parent[s1] = s2				
    set_size = set_size - 1		

def MSTKruskal(vertex, adj):		
    vsize = len(vertex)          #정점 갯수 
    init_set(vsize)              #정점 갯수만큼 부모 트리 인덱스 초기화
    eList = []                      
    addEdgeList=[]
    for i in range(vsize-1) :       
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append( (i,j,adj[i][j]) ) #정점, 연결정점, 가중치

    eList.sort(key= lambda e : e[2], reverse=True) #간선 내림차순 정렬 

    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) : #정점 수만큼 반복 
        e = eList.pop(-1)      #정점리스트의 성분이 줄어들기 때문에(pop을 쓰므로) 내림차순정렬하고 뒤에부터 뽑음 		
        uset = find(e[0])      			
        vset = find(e[1])

        if uset != vset :       		
            addEdgeList.append(e[2]) #가중치를 리스트에 담음
            totalWeight=sum(addEdgeList) #가중치 합
            print("간선 추가 : (%s, %s, %d), 가중치합: %d" %(vertex[e[0]], vertex[e[1]], e[2],totalWeight))
            union(uset, vset)   	
            edgeAccepted += 1   	

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)