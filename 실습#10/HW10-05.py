#5. 인접리스트(딕셔너리 + 집합)으로 표현된 그래프에 대해 위상정렬 알고리즘 구현
# inDeg는 딕셔너리로 처리할 것
mygraph = { "A" : set(["C","D"]),
            "B" : set(["D", "E"]),
            "C" : set(["D", "F"]),
            "D" : set(["F"]),
            "E" : set(["F"]),
            "F" : set()
          } #딕셔너리와 집합으로 표현됨

"""
1. 차수관계를 파악해야함 (차수관계 각 정점마다 파악하여 하나의 리스트로 정리)
2. 차수 0인 곳 공략 
3. 하나의 정점을 공략한 후에는 정점과 간선을 삭제시켜야함
4. 그 후 다음 정점들의 차수를 떨궈야함
"""

def topological_sort_List(graph):
    #차수관계파악
    inDeg={ "A" : 0, "B" : 0, "C" : 0, "D" : 0,"E" : 0, "F" : 0}#반복문으로 키값당 업데이트 하는거 해야함
    for vtx in graph: #A~H까지
        for linkNode in graph[vtx]: #연결된 접점들 관계
        #연결 노드들의 차수를 1씩증가(A는 B,C와 연결되어 있으므로 B C의 inDeg 값 1씩 증가)
            inDeg[linkNode] +=1
    
    #차수가 0인곳을 공략
    vlist=[]
    for i in inDeg:
        if inDeg[i]==0:
            vlist.append(i)
    
    while len(vlist)>0:
        v=vlist.pop()
        print(v, end=' ') # 화면에 순서출력
        for u in graph[v]: #연결 접점 차수감소
            inDeg[u]-=1
            if inDeg[u]==0:
                vlist.append(u)
                
topological_sort_List(mygraph)