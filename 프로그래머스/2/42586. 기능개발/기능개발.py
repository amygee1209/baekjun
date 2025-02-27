from collections import deque
import math

def solution(progresses, speeds):
    result = []
    
    workTimeQueue = deque()
    for i in range(len(progresses)):
        workTime = math.ceil((100-progresses[i])/speeds[i])
        workTimeQueue.append(workTime)
    
    untilNextDeploy = workTimeQueue[0]
    deployAmount = 0
    while workTimeQueue:
        workTime = workTimeQueue.popleft()
        if workTime <= untilNextDeploy:
            deployAmount += 1
        else:
            result.append(deployAmount)
            untilNextDeploy = workTime
            workTimeQueue.appendleft(workTime)
            deployAmount = 0
    
    result.append(deployAmount)
    return result
        
            