from collections import deque

def solution(s):
    stack = deque([])
    for letter in s:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    if len(stack) < 1:
        return 1
    return 0