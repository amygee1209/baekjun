from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucksInLine = deque(truck_weights)
    onBridge = deque([0] * bridge_length)
    onBridgeWeightTotal = 0
    totalTime = 0
    
    while trucksInLine or onBridgeWeightTotal > 0:
        poppedTruck = onBridge.popleft()
        onBridgeWeightTotal -= poppedTruck
        
        if trucksInLine:
            if onBridgeWeightTotal + trucksInLine[0] <= weight:
                nextTruck = trucksInLine.popleft()
                onBridge.append(nextTruck)
                onBridgeWeightTotal += nextTruck
            else:
                onBridge.append(0)
        totalTime += 1
    return totalTime