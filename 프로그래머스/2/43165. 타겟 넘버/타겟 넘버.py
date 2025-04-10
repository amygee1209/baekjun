from collections import deque

def solution(numbers, target):
    N = len(numbers)
    
    def dfs(index, remainderTarget):
        if index >= N-1:
            if abs(remainderTarget) == numbers[index]:
                return 1
            else:
                return 0
        
        currentNumber = numbers[index]
        return dfs(index+1, remainderTarget-currentNumber) + dfs(index+1, remainderTarget+currentNumber)
    
    return dfs(0, target)