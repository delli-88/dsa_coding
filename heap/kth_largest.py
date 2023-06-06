from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(k):
            heap.append(nums[i])
        
        heapq.heapify(heap)

        for i in range(k,len(nums)):
            if nums[i]>=heap[0]:
                heapq.heappushpop(heap,nums[i])
        
        return heap[0]

print(Solution().findKthLargest(nums =[5,2,4,1,3,6,0], k = 4))


'''
Problem : https://leetcode.com/problems/kth-largest-element-in-an-array
TC - O((n-k)logk)
SC - O(k)
Approach:
1.Initialize an empty heap.
2.Add the first k elements from the input list nums to the heap.
3.Convert the heap into a min-heap using heapify operation.
4.Iterate over the remaining elements from index k to n-1 in nums.
    4a.If the current element is greater than or equal to the smallest element in the heap (heap[0]), replace the smallest element in the heap with the current element using the heappushpop operation.
5.After processing all the elements, the kth largest element will be the smallest element in the heap.
6.Return the smallest element in the heap as the kth largest element.
'''