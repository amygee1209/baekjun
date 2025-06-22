def solution(a, b, g, s, w, t):
    numOfCities = len(g)
    maxTime = max(t) * (a+b) * 2
    # print(maxTime)
    
    minTime = 1
    answer = 0
        
    while minTime <= maxTime:
        midTime = (minTime + maxTime) // 2
        totalA, totalB, totalBoth = 0, 0, 0
        for i in range(numOfCities):
            numOfOneWayTrips = midTime // (2 * t[i])
            if midTime % (2 * t[i]) >= t[i]:
                numOfOneWayTrips += 1
            totalA += min(g[i], numOfOneWayTrips * w[i])
            totalB += min(s[i], numOfOneWayTrips * w[i])
            totalBoth += min(g[i]+s[i], numOfOneWayTrips * w[i])
        if totalBoth >= (a+b) and totalA >= a and totalB >= b:
            answer = midTime
            maxTime = midTime - 1
        else:
            minTime = midTime + 1
            
    return answer