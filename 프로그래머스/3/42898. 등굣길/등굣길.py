def solution(m, n, puddles):
    MOD = 1000000007
    puddlesTuple = set((r-1,c-1) for c, r in puddles)
    if (0, 0) in puddlesTuple:
        return 0
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    # print(dp)
    for i in range(n):
        for j in range(m):
            if (i==0 and j==0) or (i, j) in puddlesTuple:
                continue
            top, left = 0, 0
            if i-1 >= 0:
                top = dp[i-1][j]
            if j-1 >= 0:
                left = dp[i][j-1]
            dp[i][j] = (left + top) % MOD
    # print(dp)
    return dp[n-1][m-1]