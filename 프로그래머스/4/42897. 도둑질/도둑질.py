def solution(money):
    def getDp(houseList):
        n = len(houseList)
        dp = [0] * n
        dp[0] = houseList[0]
        dp[1] = max(houseList[0], houseList[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + houseList[i])
        return dp
    noFirstHouseDp = getDp(money[1:])
    noLastHouseDp = getDp(money[:-1])   
    
    return max(noFirstHouseDp[-1], noLastHouseDp[-1])