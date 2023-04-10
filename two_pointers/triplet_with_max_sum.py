from typing import List

def maxSumTriplet(n: int, arr: List[int]) -> int:
    maxi = 0
    for j in range(1,n-1):
        middle = arr[j]

        first = 0
        for i in range(j):
            if arr[i]<middle and arr[i]>first:
                first = arr[i]
        
        last = 0
        for k in range(j+1,n):
            if arr[k]>middle and arr[k]>last:
                last = arr[k]
        
        if first!=0 and last!=0:
            maxi = max(maxi,first+middle+last)

    return maxi
"""
Problem: https://www.geeksforgeeks.org/find-maximum-sum-triplets-array-j-k-ai-aj-ak/
TC - O(n^2)
SC - O(1)
Approach :
 we loop through second to last but one element
    and we consider the curr element to be the middle element and we fix this
    now we find the max left and max right satisfying the conditions
    if found we check and update maxi
return maxi
"""