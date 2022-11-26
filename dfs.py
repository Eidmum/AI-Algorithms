# graph = {
#     '1': ['4', '2'],
#     '2': ['1','3','5','8'],
#     '3': ['2','4','9','10'],
#     '4': ['1','3'],
#     '5':['2','8','7','6'],
#     '6':['5'],
#     '7':['5','8'],
#     '8':['2','7','5'],
#     '9':['3'],
#     '10':['3']
#
#
# }
# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }
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
def dfs(node):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for i in graph[node]:
            dfs(i)

dfs('H')

