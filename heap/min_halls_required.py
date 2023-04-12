import heapq
from typing import List
def meetingRooms(meetings: List[List[int]]) -> int:
    meetings.sort(key=lambda x:x[0])
    heap  = [meetings[0][1]]
    for i in range(1,len(meetings)):
        start = meetings[i][0]
        end = meetings[i][1]
        if start>=heap[0]:
            heapq.heappushpop(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


"""
Problem : https://www.geeksforgeeks.org/minimum-halls-required-for-class-scheduling/
TC - O(nlogn)
SC - O(n)
Optimal Approach:
We can use MinHeap
we loop through the array
    if the start time of curr meeting is greater than or eq to min_heap(it means one of the meetings is over and we can use that room)
        remove that min_heap ele and push the new meeting end time into heap
    else:
        we push the curr_meeting's end time into heap

"""