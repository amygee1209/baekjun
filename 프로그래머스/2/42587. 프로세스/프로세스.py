from collections import deque
import heapq

def solution(priorities, location):
    operationList = deque([i for i in range(len(priorities))])
    maxheap = []
    executionList = []
    
    for index, priority in enumerate(priorities):
        heapq.heappush(maxheap, (-priority, index))
        
    while operationList:
        operation = operationList.popleft()
        highestPriority , highestPriorityIndex = heapq.heappop(maxheap)
        if priorities[operation] < -highestPriority:
            operationList.append(operation)
            heapq.heappush(maxheap, (highestPriority , highestPriorityIndex))
        else:
            executionList.append(operation)
            
    for index, exec in enumerate(executionList):
        if location == exec:
            return index+1