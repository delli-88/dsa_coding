from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 50
        sol = [0] * (len(nums) - k + 1)
        for i in range(len(nums)):
            if nums[i] < 0: 
                freq[nums[i] + 50] += 1
            if i - k >= 0 and nums[i - k] < 0: 
                freq[nums[i - k] + 50] -= 1
            if i - k + 1 < 0: 
                continue
            neg_count = 0
            for j in range(50):
                neg_count += freq[j]
                if neg_count >= x:
                    sol[i - k + 1] = j - 50
                    break
        return sol

'''
Problem : https://leetcode.com/problems/sliding-subarray-beauty
TC - O(n*50) -> O(n)
SC - O(max(O(50),n - k + 1)))
Approach : 
As the constraints are less i.e. -50 to 50,
We keep track of number of negative elements in a window
we inc the freq of neg elements
and we loop through the freq array, and we can append the nth smallest 

'''