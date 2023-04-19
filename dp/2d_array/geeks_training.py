# dp-tabulation-space-optimization
class Solution:
    def maximumPoints(self, points, n):
        dp_prev = [-1 for _ in range(3)]
        maxi = 0
        for r0 in range(3):
            dp_prev[r0] = max(points[0][(r0+1)%3],points[0][(r0+2)%3])
            maxi = max(maxi,dp_prev[r0])
        if n==1:
            return maxi
        maxi = 0
        for day in range(1,n):
            dp_curr = [-1 for _ in range(3)]
            for activity in range(3):
                dp_curr[activity] =  max(points[day][(activity+1)%3]+dp_prev[(activity+1)%3], points[day][(activity+2)%3]+dp_prev[(activity+2)%3]) 
                if day==n-1:
                    maxi = max(maxi, dp_curr[activity])
            dp_prev = dp_curr
        return maxi
'''
Problem : https://practice.geeksforgeeks.org/problems/geeks-training/1
TC - O(n*3) 
SC - O(3) -> O(1)
Optimal Approach:
Same as tabulation, nut instead of storing n days, we just store the previous days max points

'''


'''
# dp-tabulation
class Solution:
    def maximumPoints(self, points, n):
        dp = [[-1 for _ in range(3)] for _ in range(len(points))]
        maxi = 0
        for r0 in range(3):
            dp[0][r0] = max(points[0][(r0+1)%3],points[0][(r0+2)%3])
            maxi = max(maxi,dp[0][r0])
        if n==1:
            return maxi
        maxi = 0
        for day in range(1,n):
            for activity in range(3):
                dp[day][activity] =  max(points[day][(activity+1)%3]+dp[day-1][(activity+1)%3], points[day][(activity+2)%3]+dp[day-1][(activity+2)%3]) 
                if day==n-1:
                    maxi = max(maxi, dp[day][activity])
        return maxi

'''
'''
Approach for dp-tabulation:
At a particular day of particular activity of dp, we store, the max points of other two activities
So what it means is that, if we choose dp[1][2], we actually get the max points on day 1 without including activity 2.
'''


'''
# dp-memoization
class Solution:
    def maximumPoints(self, points, n):
        dp = [[-1 for _ in range(3)] for _ in range(len(points))]

        return self.maximumPointsHelper(points,n-1,-1,dp)

    def maximumPointsHelper(self,points,day,activity, dp):
        if dp[day][activity]!=-1:
            return dp[day][activity]
        
        if day==0:
            maxi = 0
            for act in range(3):
                if act!=activity:
                    maxi = max(maxi, points[day][act])
            dp[day][activity] = maxi
            return dp[day][activity]
        
        
        maxi = 0
        for act in range(3):
            if act!=activity:
                maxi = max(maxi, self.maximumPointsHelper(points,day-1,act,dp)+ points[day][activity])
        
        dp[day][activity] = maxi 

        return dp[day][activity]
'''

print(Solution().maximumPoints([[1,2,5],[3,1,1],[3,3,3]],3))