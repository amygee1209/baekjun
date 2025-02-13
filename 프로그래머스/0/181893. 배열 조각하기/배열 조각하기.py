def solution(arr, query):
    result = arr.copy()
    for i in range(len(query)):
        index = query[i]
        if i % 2 == 0:
            tmp = result[:index+1]
            result = tmp.copy()
        else:
            tmp = result[index:]
            result = tmp.copy()
    return result