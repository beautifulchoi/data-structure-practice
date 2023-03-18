#6 브리지 찾아 출력하는 함수 만들기 
mygraph = { "A" : set(["B","C"]),
            "B" : set(["A", "D"]),
            "C" : set(["A", "D", "E"]),
            "D" : set(["B", "C", "F"]),
            "E" : set(["C", "G", "H"]),
            "F" : set(["D"]),
            "G" : set(["E", "H"]),
            "H" : set(["E", "G"])
          }

def find_connected_component(graph) :
    visited = set()					
    colorList = []					

    for vtx in graph :				
        if vtx not in visited :		
            color = dfs_cc(graph, [], vtx, visited)	
            colorList.append( color )	
    return len(colorList)
			        
def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited :				
        visited.add(vertex)					
        color.append(vertex)				
        nbr = graph[vertex] - visited		
        for v in nbr:						
            dfs_cc(graph, color, v, visited)
    return color	

#예제에서 만든 성분검사 함수를 이용하여, 각 정점의 간선을 제거해 본 후, 성분이 2개로 나뉘게 되면 브릿지
for vtx in mygraph:
    for comp in mygraph[vtx]:
        mygraph[vtx].discard(comp) #간선제거
        det=find_connected_component(mygraph) #성분 몇개인지 확인
        if det>1: #성분 2개로 나뉘게 되면
            print(vtx,comp) #브릿지이므로 출력 
        mygraph[vtx].add(comp) # 다시 원상복구 
        