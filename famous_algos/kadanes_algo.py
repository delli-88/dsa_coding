from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr_sum = nums[0]
        max_till_now = nums[0]
        for i in range(1,len(nums)):
            max_till_now = max(nums[i],max_till_now+nums[i])
            if max_till_now>max_sub_arr_sum:
                max_sub_arr_sum = max(max_sub_arr_sum,max_till_now)
        return max_sub_arr_sum

"""
Problem : https://leetcode.com/problems/maximum-subarray/
TC - O(n)
SC - O(1)
Optimal Approach:
we run a loop 
    at every index, check and update max_till_now, when the subarray becomes maximum 
        i) if curr_ele is added to  max_till_now or
        ii) if just curr_ele itself is greater than adding it to max_till_now
    and if max_till_now is greater than global max, then update it
return global max                                           
"""