def solution(number, k):
    numberStack = []
    
    for digit in number:
        while numberStack and numberStack[-1] < digit and k > 0:
            numberStack.pop()
            k -= 1
        numberStack.append(digit)
    while k > 0:
        numberStack.pop()
        k -= 1
    return "".join(numberStack)