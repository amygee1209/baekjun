def solution(elements):
    N = len(elements)
    subTotal = set()
    intervalSumList = [0] * (N+1)
    
    for i in range(N):
        intervalSumList[i+1] = intervalSumList[i] + elements[i]
    
    for size in range(N):
        for left in range(N):
            right = left + size
            if right < N:
                intervalSum = intervalSumList[right+1] - intervalSumList[left]
            else:
                right %= N
                intervalSum = intervalSumList[N] - intervalSumList[left] + intervalSumList[right+1]
            subTotal.add(intervalSum)
    return len(subTotal)