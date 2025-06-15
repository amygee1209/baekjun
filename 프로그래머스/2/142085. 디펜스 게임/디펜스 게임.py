import heapq

def solution(n, k, enemy):
    
    N = len(enemy)
    if k >= N:
        return N
    
    heapQueue = [enemy[i] for i in range(k)]
    heapq.heapify(heapQueue)
    
    for i in range(k, N):
        heapq.heappush(heapQueue, enemy[i])
        smallestEnemy = heapq.heappop(heapQueue)
        if n >= smallestEnemy:
            n -= smallestEnemy
        else:
            return i
            
    return N
        