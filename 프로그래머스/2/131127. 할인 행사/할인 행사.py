def solution(want, number, discount):
    
    myWantCount = {}
    for i in range(len(want)):
        myWantCount[want[i]] = number[i]
        
    numOfDays = 0
    
    N = len(discount)
    discountItemCount = {}
    for discountItem in discount[:10]:
        discountItemCount[discountItem] = discountItemCount.get(discountItem, 0) + 1
    
    for i in range(N-9):
        validDay = True
        for want, number in myWantCount.items():
            if number > discountItemCount.get(want, 0):
                validDay = False
                break
        if validDay:
            numOfDays += 1
        if (i+10) < N:
            discountItemCount[discount[i]] -= 1
            discountItemCount[discount[i+10]] = discountItemCount.get(discount[i+10], 0) + 1
            
    return numOfDays
        