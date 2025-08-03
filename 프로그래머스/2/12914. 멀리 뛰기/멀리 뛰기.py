def solution(n):
    MOD = 1234567

    # n이 1일 때의 예외 처리
    if n == 1:
        return 1

    # dp 배열 초기화
    dp = [0] * (n + 1)
    
    # 기본 값 설정
    dp[1] = 1
    dp[2] = 2

    # DP 테이블 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]