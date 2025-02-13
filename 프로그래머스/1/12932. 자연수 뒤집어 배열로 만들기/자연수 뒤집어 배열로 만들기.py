def solution(n):
    result = []
    while n > 0:
        num = n % 10
        n //= 10
        result.append(num)
    return result