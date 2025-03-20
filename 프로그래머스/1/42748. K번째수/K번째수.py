def solution(array, commands):
    result = []
    
    for c in commands:
        [i, j, k] = c
        sortedPartialArray = sorted(array[i-1:j])
        result.append(sortedPartialArray[k-1])
    return result