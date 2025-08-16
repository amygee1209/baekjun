from collections import deque, defaultdict

def solution(n, edge):
    pathLength = [0] * (n+1)
    graph = defaultdict(list)
    for e in edge:
        nodeA, nodeB = e
        graph[nodeA].append((nodeA, nodeB))
        graph[nodeB].append((nodeB, nodeA))
    queue = deque(graph[1])
    lastVisitedNode = [0] * (n+1)
    lastVisitedNode[1] = 1
    while queue:
        nodeStart, nodeEnd = queue.popleft()
        if lastVisitedNode[nodeEnd] > 0: continue
        lastVisitedNode[nodeEnd] = nodeStart
        pathLength[nodeEnd] = pathLength[nodeStart] + 1
        for nextNodeStart, nextNodeEnd in graph[nodeEnd]:
            if lastVisitedNode[nextNodeEnd] == 0:
                queue.append((nextNodeStart, nextNodeEnd))
    maxPathLength = max(pathLength[1:])
    maxPathNode = [length for length in pathLength[1:] if length == maxPathLength]
    return len(maxPathNode)
    