from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    
    pathCnts = []
    visited = set()
    queue = deque([(0, 0, 1)])
    
    while queue:
        r, c, cnt = queue.popleft()
        if r == n-1 and c == m-1:
            return cnt
        if (r, c) not in visited:
            visited.add((r, c))
            
            for dirR, dirC in directions:
                nextR, nextC = r+dirR, c+dirC
                if 0 <= nextR < n and 0 <= nextC < m and maps[nextR][nextC] == 1 and (nextR, nextC) not in visited:
                    queue.append((nextR, nextC, cnt+1))
                    
    return -1