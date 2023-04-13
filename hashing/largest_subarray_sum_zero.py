from typing import List
def largestSubarraySumZero(n: int, arr: List[int]) -> List[int]:
    freq = {0:-1}
    max_index = 0
    max_len = 0
    prefix_sum = 0
    for i in range(n):
        prefix_sum+=arr[i]
        if freq.get(prefix_sum)!=None:
            curr_len =  i-freq.get(prefix_sum)
            if curr_len>max_len:
                max_len = curr_len
                max_index = freq.get(prefix_sum) + 1
        else:
            freq[prefix_sum] = i
    
    sol = []
    for s in range(max_index,max_index+max_len):
        sol.append(arr[s])
    
    return sol

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = largestSubarraySumZero(n, arr)
    print(*result)

if __name__=="__main__":
    main()

"""
Problem : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
TC - O(n)
SC - O(n)
Optimal Approach:
We run a loop for n times
    we calculate prefix sum
    we look if the prefix sum is already present in our freq dictionary
        if it is present that means we have found a subarray with sum zero , we check and update the max_length if curr_len is greater, and also store the starting index.
        else we just add the prefix sum as key and it's index as val in our dictionary
after loop, we have the length of max_sub array and the starting index of our max sub array, from these details, we print the max_sub_array
return sol
"""