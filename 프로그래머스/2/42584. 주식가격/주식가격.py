from collections import deque

def solution(prices):
    stack = deque([])
    result = [-1] * len(prices)
    for i, v in enumerate(prices):
        while stack and prices[stack[-1]] > v:
            lastIndex = stack.pop()
            result[lastIndex] = i - lastIndex
        stack.append(i)
    while stack:
        lastIndex = stack.pop()
        result[lastIndex] = len(prices) - 1 - lastIndex
    return result