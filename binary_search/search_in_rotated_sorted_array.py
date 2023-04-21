from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid

            if nums[mid]< nums[end]:
                if target>nums[mid] and target<= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if target<nums[mid] and target>= nums[start]:
                    end = mid-1
                else:
                    start = mid+1
        return -1
    
'''
Problem : https://leetcode.com/problems/search-in-rotated-sorted-array
TC - O(logn)
SC - O(1)
Approach:
We follow binary search here
we init start to 0 and end to len-1
we do the below steps for start<=end
    we calc mid
    at any mid, if the array is sorted and rotated, either one half or the other half has to be visibly sorted
    so we check if target is present in the range of one half of sorted array
        if yes, we go and continue the binary search in this half, else, we go into other half
return -1 if not found

'''