def solution(people, limit):
    people.sort()
    N = len(people)
    left, right = 0, N-1
    boatMoveCnt = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boatMoveCnt += 1
    return boatMoveCnt