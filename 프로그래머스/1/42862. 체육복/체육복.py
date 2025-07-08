from collections import deque

def solution(n, lost, reserve):
    setLost = set(lost)
    setReserve = set(reserve)
    actualLost = setLost - setReserve
    actualReserve = setReserve - setLost
    lostQueue = deque(sorted(actualLost))
    reserveQueue = deque(sorted(actualReserve))
    stillLostCnt = 0
    
    while lostQueue and reserveQueue:
            
        if abs(lostQueue[0] - reserveQueue[0]) <= 1:
            lostQueue.popleft()
            reserveQueue.popleft()
            continue
            
        if lostQueue[0] < reserveQueue[0]:
            lostQueue.popleft()
            stillLostCnt += 1
        else:
            reserveQueue.popleft()
    
    return n - len(lostQueue) - stillLostCnt