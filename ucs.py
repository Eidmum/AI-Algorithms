graph={
    's': [['a',2],['b',5]],
    'a': [['c',2],['d',4]],
    'b': [['g',5]],
    'c':[['d',3]],
    'd':[['g',2]],
    'g':[]

};
queue=[]


def ucs(start,end):
    minimumCostIndex = 0
    queue.append([[start],0])
    iteration = 0
    while queue:
        currentNode=queue.pop(minimumCostIndex)
        if currentNode[0][0]==end:
            return currentNode


        for child in graph[currentNode[0][0]]:
            newNode = currentNode[0].copy()
            childNode=child[0]
            childCost=child[1]
            newNode.insert(0, childNode)
            newCost=childCost+currentNode[1]
            queue.append([newNode,newCost])
        iteration=iteration+1
        print("After iteration number : {} the queue looks like : {}".format(iteration,queue))
        print("..................................................")
        minimumCostIndex=0
        minimumCost=queue[0][1]
        for i in range(0,len(queue)):
            if queue[i][1]<minimumCost:
                minimumCost=queue[i][1]
                minimumCostIndex=i





ans=ucs('s','g')
print("Minimum path : {}".format(ans[0]))
print("Minimum cost : {}".format(ans[1]))

