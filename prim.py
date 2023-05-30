graph = {
    'v1':[
        ('v2',1),
        ('v3',3)
    ],
    'v2':[
        ('v1',1),
        ('v3',3),
        ('v4',6)
    ],    
    'v3':[
        ('v1',3),
        ('v4',4),
        ('v2',3),
        ('v5',2)
    ],
    'v4':[
        ('v2',6),
        ('v3',4),
        ('v5',5)
    ],
    'v5':[
        ('v3',2),
        ('v4',5)
    ]
}

key = {} #keeps minimum value of each vertix to arrive.
parent = {} #keeps parent vertix of each one for helping with create branches

def prim(graph,start):
    for vert in graph:
        if vert == start:
            key[vert] = 0
        else:
            key[vert] = float('inf')
            parent[vert] = None
    
    solution = [] #this is gonna keep branches
    vertixes = list(graph.keys()) #this is using for check is every vertix done or not
    while vertixes:
        u = min(vertixes , key=lambda x:key[x]) #get minimum vertix with minimum key
        vertixes.pop(vertixes.index(u))
        for neigh in graph[u]: #foreach neighbor(near) vertix to U do
            if neigh[0] in vertixes and key[neigh[0]] > neigh[1]:
                key[neigh[0]] = neigh[1]
                parent[neigh[0]] = u
    for e in parent: #foreach branches that we found , we add them to solution list
        solution.append((parent[e],e))
    return solution
        

print(prim(graph, 'v1'))