from collections import deque

def isAdjacent(wordA, wordB):
    diffCount = 0
    for i in range(len(wordA)):
        if wordA[i] != wordB[i]:
            diffCount += 1
    return diffCount == 1

def solution(begin, target, words):
    
    adjDict = {word: [] for word in words}
    adjDict[begin] = []
    
    for i, wordA in enumerate(words):
        for j, wordB in enumerate(words):
            if i != j and isAdjacent(wordA, wordB):
                adjDict[wordA].append(wordB)
                adjDict[wordB].append(wordA)
                
    for word in words:
        if isAdjacent(begin, word):
            adjDict[begin].append(word)
            adjDict[word].append(begin)
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        node, cnt = queue.popleft()
        if node == target:
            return cnt
        visited.add(node)
        
        for adjWord in adjDict[node]:
            if not adjWord in visited:
                queue.append((adjWord, cnt+1))
        
    return 0