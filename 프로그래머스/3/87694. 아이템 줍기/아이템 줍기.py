from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for _ in range(102)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for rec in rectangle:
        xStart, yStart, xEnd, yEnd = rec
        for x in range(xStart*2, xEnd*2+1): 
            for y in range(yStart*2, yEnd*2+1):
                if xStart*2 < x < xEnd*2 and yStart*2 < y < yEnd*2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1
    # print(graph)
    visited = set()
    queue = deque([(characterX*2, characterY*2, 0)])
    
    while queue:
        node = queue.popleft()
        print(node)
        nodeX, nodeY, routeCnt = node
        if nodeX == itemX*2 and nodeY == itemY*2:
            return routeCnt//2
        
        if node not in visited:
            visited.add((nodeX, nodeY))
            for dir in directions:
                dirX, dirY = dir
                nextX = nodeX+dirX
                nextY = nodeY+dirY
                if graph[nextX][nextY] == 1 and (nextX, nextY) not in visited:
                    queue.append((nextX, nextY, routeCnt+1))
                    
    return -1
            