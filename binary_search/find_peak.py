from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)-1
        start = 0
        end = n
        while start<end:
            mid = (start+end)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid]<nums[mid+1]:
                start = mid +1
            else:
                end = mid
        return start

'''
Problem : https://leetcode.com/problems/find-peak-element
TC - O(logn)
SC - O(1)
Approach:
As conditions states we can return any peak
we follow binary search
we check the mid with neighbours, and we continue binary search in a half, where the neighbour is greater then mid
we are searching for a slope
we are sure it works beacuse, as we know the neighbour is greater than mid, then even if it is the end, then it must be the peak
'''

print(Solution().findPeakElement(nums = [5,4,3,2,1]))