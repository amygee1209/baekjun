from collections import deque

def solution(stones, k):
    maxQueue = deque()
    maxNumOfPpl = float('inf')
    
    for index, val in enumerate(stones):
        while maxQueue and stones[maxQueue[-1]] < val:
            maxQueue.pop()
            
        maxQueue.append(index)
        
        if maxQueue[0] == (index-k):
            maxQueue.popleft()
        
        if index >= (k-1):
            maxNumOfPpl = min(maxNumOfPpl, stones[maxQueue[0]])
    
    return maxNumOfPpl