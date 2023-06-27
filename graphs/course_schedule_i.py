from collections import deque
from typing import List
class Solution:
    def canFinish(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for prerequisite in prerequisites:
            course, prerequisite_course = prerequisite
            adj[prerequisite_course].append(course)
            inDegree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
        count = 0  
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in adj[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses


print(Solution().canFinish(numCourses = 5, prerequisites = [[1,2],[2,3],[3,4],[1,4]]))
'''
Problem : https://leetcode.com/problems/course-schedule/
TC - O(V + E)
SC - O(V)
Approach :
1.Create an adjacency list to represent the courses and their prerequisites. Each course will have a list of its dependent courses.
2.Initialize an array called inDegree of size numCourses and set all its elements to 0. This array will store the in-degree (number of prerequisites) for each course.
3.Iterate through the prerequisites list and update the adjacency list and in-degrees accordingly. For each prerequisite pair [ai, bi], add course ai to the adjacency list of course bi and increment the in-degree of course ai by 1.
4.Create a queue to perform the topological sorting.
5.Enqueue all the courses that have an in-degree of 0 into the queue.
6.Initialize a counter variable count to keep track of the number of courses visited.
7.While the queue is not empty, do the following:
    a.Dequeue a course from the queue.
    b.Increment the count by 1 to indicate that a course has been visited.
    c.Iterate through the adjacent courses of the dequeued course.
    d.Decrement the in-degree of each adjacent course by 1.
    e.If the in-degree of an adjacent course becomes 0, enqueue it into the queue.
8.After the while loop, check if the count is equal to numCourses. If they are equal, it means all courses have been visited and there is no cycle, so return True. Otherwise, there is a cycle, and it is not possible to finish all the courses, so return False.
'''