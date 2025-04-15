from collections import deque

def solution(n, computers):
    N = len(computers)
    
    visited = set()
    cnt = 0
    
    for curr in range(N):
        if curr not in visited:
            cnt += 1
            stack = deque([curr])

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)

                    for i, val in enumerate(computers[node]):
                        if i != node and val == 1:
                            stack.append(i)
                            
    return cnt
                