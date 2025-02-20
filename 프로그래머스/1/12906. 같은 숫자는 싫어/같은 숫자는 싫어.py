from collections import deque

def solution(arr):
    stack = deque([])
    
    for num in arr:
        while stack and stack[-1] == num:
            stack.pop()
        stack.append(num)
    return list(stack)