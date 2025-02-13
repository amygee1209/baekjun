def solution(arr, divisor):
    result = []
    for n in arr:
        if n % divisor == 0:
            result.append(n)
    if len(result) > 0:
        return sorted(result)
    else:
        return [-1]