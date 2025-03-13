def solution(sequence, k):
    
    N = len(sequence)
    
    subTotal = [0] * (N+1)
    for i in range(0, N):
        subTotal[i+1] = subTotal[i] + sequence[i]
    
    left, right = 0, 0
    result = [left, right]
    minLen = float('inf')
    while right < len(sequence):
        intervalSum = subTotal[right+1] - subTotal[left]
        if intervalSum == k:
            if (right-left+1) < minLen:
                minLen = right-left+1
                result = [left, right]
            left += 1
            right += 1
        elif intervalSum > k:
            left += 1
        else:
            right += 1
    return result