#https://ko.wikipedia.org/wiki/서로소_집합_자료_구조#유니온_바이_랭크(Union_by_rank)
parent = {}
rank = {}
def make_set(v):
    parent[v] = v
    rank[v] = 0
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
    mst = []

    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
        if find(v) != find(u):
            union(v, u)
            print(rank)
            mst.append(edge)
    
    return mst
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (15, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F'),
    ]
}
print( kruskal(graph) )