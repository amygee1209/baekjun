from collections import deque

def solution(s):
    stack = deque([])
    
    for item in s:
        if stack and stack[-1] == "(" and item == ")":
            stack.pop()
        else:
            stack.append(item)
    if len(stack) <= 0:
        return True
    else:
        return False