from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        for right_elem in range(len(nums)):
            right_sum+=nums[right_elem]
        #right sum is the total sum
        left_sum = 0
        for ele in range(len(nums)):
            pivot = nums[ele]
            right_sum-=pivot
            if left_sum==right_sum:
                return ele
            left_sum+=pivot
        return -1

"""
Problem: https://leetcode.com/problems/find-pivot-index/

TC - O(2n) -> O(n)
SC - O(1)
Optimal Approach:
We find the total sum -> right_sum
init left_sum -> 0 

loop through the array
    at every index, remove the curr_val from right_sum (so that the right sum will not contain the pivot)
    check if left_sum == right_sum, if yes, return index
            else add the curr_val to left_sum
        (so at every iteration, we are removing the curr_val from right_sum and adding the same to left_sum)
    return -1 if not found
"""


"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for p in range(1,n):
            prefix_sum[p] = prefix_sum[p-1] + nums[p]
        sufffix_sum = [0]*n
        sufffix_sum[-1] = nums[-1]
        for s in range(n-2,-1,-1):
            sufffix_sum[s] = sufffix_sum[s+1] + nums[s]

        for i in range(n):
            if i==0:
                if sufffix_sum[1]==0:
                    return i
            elif i==n-1:
                if prefix_sum[n-2]==0:
                    return i
            elif prefix_sum[i-1]==sufffix_sum[i+1]:
                return i
        return -1

TC - O(3n) -> O(n)
SC - O(2n) -> O(n)
Approach:
Find prefix sum
find suffix sum
Loop through the arr    
    at each index check if prefix of previous ind is equal to suffix of next index, if yes return True
return False

"""
    
print(Solution().pivotIndex([1,7,3,6,5,6]))