from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        sol = [intervals[0]]
        for i in range(1,len(intervals)):
            sol_top = sol[-1]
            start = intervals[i][0]
            end = intervals[i][1]
            if start<=sol_top[1]:
                if sol_top[1]<end:
                    sol_top[1] = end
            else:
                sol.append(intervals[i])
        return sol

"""
Problem : https://leetcode.com/problems/merge-intervals/
TC - O(nlogn)
SC - O(n)
Approach :
We First Sort the array
We initialize a sol array to be returned with 1st array of interval
we iterate from 1 to n of interval
    we check if curr_interval start is less than or equal to our sol's top's end (in this case merging happens)
        if yes, we merge (only if the end of curr_interval is greater than sol top's end)
        else, we append the curr_interval to our sol array, and this will become our new top
return sol
"""

print(Solution().merge(intervals = [[1,4]]))