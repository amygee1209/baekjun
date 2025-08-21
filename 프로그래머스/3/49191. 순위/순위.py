def solution(n, results):
    outcome = [[False] * n for _ in range(n)]
    for i in range(n):
        outcome[i][i] = True
    for winPlayer, losePlayer in results:
        outcome[winPlayer-1][losePlayer-1] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                outcome[i][j] = outcome[i][j] or (outcome[i][k] and outcome[k][j])
    for i in range(n):
        for j in range(n):
            outcome[i][j] = outcome[i][j] or outcome[j][i]
    cnt = 0
    for i in range(n):
        if all(outcome[i]):
            cnt += 1
    print(outcome)
    
    return cnt
        
        