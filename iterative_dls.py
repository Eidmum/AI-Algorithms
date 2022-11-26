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
desired_level=int(input("Enter your desired level : "))
for i in range(0,desired_level+1):
    level_limit = i
    print("The iterative dls path for level limit {} is : ".format(level_limit))
    dls('H', 0)
    print()
    visited=[]




