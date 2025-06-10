from collections import deque, defaultdict

def dfs(stack, visited, computers, computerNetworks):
    
    while stack:
        currentComputerIndex = stack.pop()
        if visited[currentComputerIndex]: continue

        visited[currentComputerIndex] = True

        for neighborComputerIndex in  computerNetworks[currentComputerIndex]:
            if visited[neighborComputerIndex]: continue

            if computers[neighborComputerIndex][currentComputerIndex]:
                stack.append(neighborComputerIndex)
                    
def solution(n, computers):
    
    computerNetworks = defaultdict(list)
    
    for currentComputerIndex, neighborComputers in enumerate(computers):
        for neighbotComputerIndex, neighborComputerIsConnected in enumerate(neighborComputers):
            if currentComputerIndex == neighbotComputerIndex: continue
            
            if neighborComputerIsConnected:
                computerNetworks[currentComputerIndex].append(neighbotComputerIndex)
    
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        if visited[i]: continue
        cnt += 1
        dfs([i], visited, computers, computerNetworks)
                            
    return cnt
                