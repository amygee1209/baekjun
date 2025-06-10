from collections import deque

def dfs(row, col, N, board, filledVal):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    stack = deque([(row, col)])
    adjList = []

    while stack:
        nodeR, nodeC = stack.pop()
        if board[nodeR][nodeC] == filledVal:
            adjList.append([nodeR, nodeC])
        board[nodeR][nodeC] = -1
        for dirR, dirC in dirs:
            nextR, nextC = nodeR+dirR, nodeC+dirC
            if 0<=nextR<N and 0<=nextC<N and board[nextR][nextC] == filledVal:
                stack.append((nextR, nextC))
    minR = min(lst[0] for lst in adjList)
    minC = min(lst[1] for lst in adjList)
    tupleAdjList = []
    for lst in adjList:
        tupleAdjList.append((lst[0] - minR, lst[1] - minC))
    return tuple(sorted(tupleAdjList)), board

def getRotatedList(itemList):
    R = max(lst[0] for lst in itemList)+1
    C = max(lst[1] for lst in itemList)+1

    rotate90List = []
    rotate180List = []
    rotate270List = []
    for itemR, itemC in itemList:
        rotate90List.append((itemC, R-1-itemR))
        rotate180List.append((R-1-itemR, C-1-itemC))
        rotate270List.append((C-1-itemC, itemR))

    return [tuple(sorted(itemList)), tuple(sorted(rotate90List)), tuple(sorted(rotate180List)), tuple(sorted(rotate270List))]

def solution(gameBoard, table):
    
    gameBoardShapes = []
    tableShapes = []
    N = len(gameBoard)
    gameBoardItems = {}
    tableItems = []
    for r in range(N):
        for c in range(N):
            if gameBoard[r][c] == 0:
                gameBoardItem, gameBoard = dfs(r,c,N,gameBoard,0)
                gameBoardItems[gameBoardItem] = gameBoardItems.get(gameBoardItem, 0) + 1
            if table[r][c] == 1:
                tableItem, table = dfs(r,c,N,table,1)
                tableItems.append(tableItem)      
               
    cnt = 0
        
    for tableItem in tableItems:
        rotatedList = getRotatedList(tableItem)
        for lst in rotatedList:
            if gameBoardItems.get(lst, 0) > 0:
                cnt += len(lst)
                gameBoardItems[lst] -= 1
                break
                
    return cnt     