from collections import defaultdict, deque

def solution(n, costs):
    parent = [i for i in range(n)]
    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node
    def union(nodeA, nodeB):
        if find(nodeA) == find(nodeB):
            return
        rootOfNodeA, rootOfNodeB = find(nodeA), find(nodeB)
        biggerNodeRoot, smallerNodeRoot = max(rootOfNodeA, rootOfNodeB), min(rootOfNodeA, rootOfNodeB)
        parent[biggerNodeRoot] = smallerNodeRoot
    
    sortedCosts = sorted(costs, key=lambda cost: cost[2])
    # graph = defaultdict(list)
    # for cost in costs:
    #     islandOne, islandTwo, crossCost = cost
    #     graph[islandOne].append((islandTwo, crossCost))
    #     graph[islandTwo].append((islandOne, crossCost))
    # print(graph)
    totalCost = 0
    totalEdges = 0
    for c in sortedCosts:
        if totalEdges >= n:
            break
        nodeA, nodeB, weight = c
        if find(nodeA) == find(nodeB):
            continue
        union(nodeA, nodeB)
        totalCost += weight
        totalEdges += 1
    return totalCost
        
    