import heapq

def solution(n, times):
    # timeHeapq = [(t, t) for t in times]
    # heapq.heapify(timeHeapq)
    # for person in range(n):
    #     cumulativeTime, timeUsed = heapq.heappop(timeHeapq)
    #     heapq.heappush(timeHeapq, (cumulativeTime + timeUsed, timeUsed))
    # return max([t[0]-t[1] for t in timeHeapq])
    
    left, right = 1, max(times) * n
    
    answer = right
    
    while left <= right:
        mid = (left+right) // 2
        numOfPeopleProcessed = 0
        for t in times:
            numOfPeopleProcessed += (mid // t)
        if n <= numOfPeopleProcessed:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer
    