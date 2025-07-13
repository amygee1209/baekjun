def solution(name):
    N = len(name)
    if set(name) == {'A'}:
        return 0
    moveCursorUpDownCountList = [0] * N
    
    for i in range(N):
        aToCharDiff = ord(name[i]) - ord('A')
        charToZDiff = ord('Z') - ord(name[i]) + 1
        moveCursorUpDownCount = min(aToCharDiff, charToZDiff)
        moveCursorUpDownCountList[i] = moveCursorUpDownCount
    
    moveCursorLeftRightCount = N-1
    for i in range(N-1, -1, -1):
        if name[i] == 'A':
            moveCursorLeftRightCount -= 1
        else:
            break
            
    for i in range(N):
        nextNonAIndex = i + 1
        while nextNonAIndex < N and name[nextNonAIndex] == 'A':
            nextNonAIndex += 1
        endToLastNonA = N-nextNonAIndex-1
            
        moveToEndAtI = 2 * i + 1 + endToLastNonA
        moveToStartAtNextNonAIndex = 1 + 2 * endToLastNonA + 1 + i
        
        moveCursorLeftRightCount = min(moveCursorLeftRightCount, moveToEndAtI, moveToStartAtNextNonAIndex)
        
    return sum(moveCursorUpDownCountList) + moveCursorLeftRightCount