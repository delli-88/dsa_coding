from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_area = 0

        while start<end:
            area = min(height[start],height[end])*(end-start)
            max_area = max(max_area,area)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return max_area

"""
TC - O(n)
SC - O(1)
Problem : https://leetcode.com/problems/container-with-most-water/
Approach :
By using two pointer approach
The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, Increasing the distance between the lines will increase the area.
Take two pointers, one at the beginning and one at the end of the input height array and maintain a variable maxarea to store the maximum area obtained till now. At every step, we find out the area formed between the values at the two pointers, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.
"""