from math import inf
from typing import List
def maximumSubarraySumSizeK(arr: List[int],n: int,k: int) -> int:

    curr_window_sum = 0
    max_window_sum = -inf
    for i in range(k):
        curr_window_sum+=arr[i]
    max_window_sum = max(max_window_sum,curr_window_sum)
    for j in range(k,n):
        curr_window_sum += (arr[j] - arr[j-k])
        max_window_sum = max(max_window_sum,curr_window_sum)

    return max_window_sum

def main():
    NK = list(map(int,input().strip().split()))
    nums = list(map(int,input().strip().split()))
    
    result = maximumSubarraySumSizeK(nums,NK[0],NK[1])
    print(result)

if __name__=="__main__":
    main()

"""
Problem : https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
TC - O(n)
SC - O(1)
Optimal Approach
We first find the sum of first k window size 
We loop from index k+1 to n
    at each iteration, we add the current element into our window and remove the starting element of our window
    and find sum and if it is greater, update max_sum 
return max_sum
"""
