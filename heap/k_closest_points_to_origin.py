from typing import List
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            x = points[i][0]
            y = points[i][1]
            dist = sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, i))
        
        for i in range(k, len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = sqrt(x**2 + y**2)
            if dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist, i))

        sol = []
        for i in range(k):
            sol.append(points[heap[i][1]])
        return sol


'''
Problem : https://leetcode.com/problems/k-closest-points-to-origin/
TC - O(k log k + (n - k) log k) => O(n log k)
SC - O(k)
Approach :
1.Create an empty heap to store the k closest points.
2.Iterate through the points:
    2a.For the first k points, calculate the Euclidean distance from the origin and push the negative distance along with the index of the point into the heap.
    2b.For subsequent points, calculate the Euclidean distance and compare it with the distance of the point at the top of the heap (i.e., the farthest point). If the current point is closer, pop the farthest point from the heap and push the current point.
3.After processing all the points, extract the k closest points from the heap and return them as the result.
'''