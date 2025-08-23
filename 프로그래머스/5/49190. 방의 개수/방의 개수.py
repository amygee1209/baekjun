from collections import defaultdict, deque

def solution(arrows):
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    edges = defaultdict(list)
    startCoor = (0, 0)
    currCoor = startCoor
    for a in arrows:
        oneStepCoor = (currCoor[0]+ dir[a][0], currCoor[1]+ dir[a][1])
        twoStepCoor = (currCoor[0]+ 2*dir[a][0], currCoor[1]+ 2*dir[a][1])
        edges[currCoor].append(oneStepCoor)
        edges[oneStepCoor].append(currCoor)
        edges[oneStepCoor].append(twoStepCoor)
        edges[twoStepCoor].append(oneStepCoor)
        currCoor = twoStepCoor
    # print(edges)
    
    numOfShapes = 0
    visitedEdge = set()
    visitedNode = set(startCoor)
    stack = [(startCoor, startCoor)]
    while stack:
        prevNode, currNode = stack.pop()
        if currNode in visitedNode and (prevNode, currNode) not in visitedEdge: 
            numOfShapes += 1
        
        visitedNode.add(currNode)
        visitedEdge.add((prevNode, currNode))
        for nextNode in edges[currNode]:
            if nextNode not in visitedNode:
                stack.append((currNode, nextNode))
        
    return numOfShapes