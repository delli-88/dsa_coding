
from typing import List
def minimumPlatforms(n: int,arrival: List[int],departure: List[int]) -> int:
    arrival.sort()
    departure.sort()

    arrival_ptr = 0
    departure_ptr = 0
    num_platforms  = 0
    max_platforms = 0

    while arrival_ptr<n:
        if arrival[arrival_ptr]<=departure[departure_ptr]:
            num_platforms+=1
            max_platforms = max(max_platforms,num_platforms)
            arrival_ptr+=1
        else:
            while departure[departure_ptr]<arrival[arrival_ptr] and departure_ptr < n:
                departure_ptr+=1
                num_platforms-=1
    return max_platforms


print(minimumPlatforms(6,[120,50,550,200,700,850],[600,550,700,500,900,1000]))

'''
TC - O(nlogn)
SC - O(1)
Approach :
1.Sort the arrival and departure times in ascending order.
2.Initialize pointers arrival_ptr and departure_ptr to 0, and num_platforms and max_platforms to 0.
3.Iterate over the arrival times:
    3a.If the current arrival time is less than or equal to the current departure time, it means a train has arrived and requires a platform. Increment num_platforms and update max_platforms if necessary. Move the arrival pointer to the next arrival time.
    3b.Otherwise, it means the next train is departing before the arrival of the current train. In this case, increment the departure pointer and decrement num_platforms to free up a platform.
4.Return max_platforms, which represents the minimum number of platforms required.
'''