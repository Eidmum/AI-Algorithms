graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited=[]
queue=[]
def bfs(node):
   queue.append(node)
   while queue:
       ans=queue.pop(0)
       if ans not in visited:
           print(ans,end=" ")
           visited.append(ans)
           for i in graph[ans]:
               queue.append(i)
bfs('5')
