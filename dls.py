graph={
    'A':['B','D'],
    'B':['C','F'],
    'C':['E','G','H'],
    'G':['E','H'],
    'E':['B','F'],
    'F':['A'],
    'D':['F'],
    'H':['A']
}
visited=[]
def dls(node,level):
    if level>level_limit:
        return
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for i in graph[node]:
            dls(i,level+1)
level=0
level_limit=3
dls('H',level)


