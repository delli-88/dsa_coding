from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_counter = 0
        max_ones = 0
        left_ptr = 0
        for i in range(len(nums)):
            if nums[i]==0 and  zero_counter<k:
                zero_counter+=1
            elif nums[i]==0 and zero_counter>=k:
                max_ones = max(max_ones,i - left_ptr)
                while left_ptr<i and nums[left_ptr]!=0:
                    left_ptr+=1
                left_ptr+=1
        max_ones = max(max_ones,i-left_ptr+1)
        return max_ones

'''
Problem : https://leetcode.com/problems/max-consecutive-ones-iii/
TC - O(n)
SC - O(1)
Optimal Approach :
We traverse through the array once
    if the curr_num is 1 we just ignore it as it counts for the subarray
    else its zero and 
        if zero_count is < k that means we can still count it as one and add len to subarray
        else we reduce our window size by placing the left_ptr(which is the starting point of our window)
            to the left of first zero skiping all ones (what this step means that, we are considering the curr_num to be one, and so
            we remove one of the zeros we have added in our window and we should also remove the ones left of it as we need conseq ones)
            we calc the max_len
return the max_len
'''