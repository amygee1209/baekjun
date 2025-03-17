from collections import deque

def solution(stones, k):
    intervalMax = deque()
    minOfIntervalMax = float('inf')
    
    for i, val in enumerate(stones):
        while intervalMax and stones[intervalMax[-1]] < val:
            intervalMax.pop()
        
        intervalMax.append(i)
        
        if intervalMax[0] <= (i-k):
            intervalMax.popleft()
        
        if i >= (k-1):
            minOfIntervalMax = min(minOfIntervalMax, stones[intervalMax[0]])
        
    return minOfIntervalMax
        
    