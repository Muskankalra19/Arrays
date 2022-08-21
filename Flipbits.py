def flipBits(arr, n): 
    # Write your code here
     
    maxValue = 0
    totalOnes = 0
    
    # Consider all SubArrays by using two nested two loops
    for i in range(n):
        if (arr[i] == 1): 
            totalOnes += 1
            
        count1 = 0
        count0 = 0
        for j in range(i, n):
            if (arr[j] == 1): 
                c
                ount1 += 1
            else:
                count0 += 1
            maxValue = max(maxValue, count0 - count1)
    result = totalOnes + maxValue
    return result
    pass
