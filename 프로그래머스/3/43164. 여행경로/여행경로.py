from collections import deque

def dfs(tickets, startCity, currentPath, visited, targetPathLength, allPaths):
    
    if len(currentPath) == targetPathLength:
        allPaths.append(currentPath)
        return
        
    for index, path in enumerate(tickets):
        
        start, end = path
        if not visited[index] and startCity == start:
            
            currentPath.append(end)
            visited[index] = True
            dfs(tickets, end, currentPath[:], visited, targetPathLength, allPaths)
            visited[index] = False
            currentPath.pop()

def solution(tickets):    
    
    N = len(tickets)
    visited = [False] * N
    startCity = "ICN"
    currentPath = [startCity]
    allPaths = []

    
    dfs(sorted(tickets), startCity, currentPath, visited, N+1, allPaths)
    
    return allPaths[0]
            