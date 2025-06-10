from collections import deque

def solution(numbers, target):
    N = len(numbers)
    
    stack = deque([(0, target)])
    cnt = 0
    
    while stack:
        node = stack.popleft()
        index, remainderTarget = node
        if index == N-1:
            if abs(remainderTarget) == numbers[index]:
                cnt += 1
            continue
        
        currentNumber = numbers[index]
        stack.append((index+1, remainderTarget-currentNumber))
        stack.append((index+1, remainderTarget+currentNumber))
        
    return cnt
    