import heapq

def solution(routes):
    routesDeque = [ (route[1], route[0]) for route in routes ]
    heapq.heapify(routesDeque)
    cnt = 0
    while routesDeque:
        # print(routesDeque)
        routeOut, routeIn = heapq.heappop(routesDeque)
        cameraAt = routeOut
        cnt += 1
        
        for i in range(len(routesDeque)):
            nextRouteOut, nextRouteIn = heapq.heappop(routesDeque)
            if not (nextRouteIn <= cameraAt <= nextRouteOut):
                heapq.heappush(routesDeque, (nextRouteOut, nextRouteIn))
    return cnt