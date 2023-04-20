from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>=target:
                end = mid-1
            else:
                start = mid+1
        
        if nums[start] != target:
            return [-1, -1]
        
        first_ind = start

        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<=target:
                start = mid+1
            else:
                end = mid-1
        last_ind = end

        return [first_ind,last_ind]


'''
Problem : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
TC - O(2logn) -> O(logn)
SC - O(1)
Approach:
We can use Modified Binary search twice here
We first run a binary search to find the first occurrence of target
    in this if we find a target also we keep moving end to left to find its first occuurrence
it will be present in start, we check if start is our target and store it, 
if its not the target we return -1
We then run a binary search to find the last occurrence of target
    in this if we find a target also we keep moving start to right to find its last occuurrence
it will be present in end and we store it
return the first_index and last_index
'''

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
