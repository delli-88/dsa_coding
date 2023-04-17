def longestSubarrayHavingSumK(arr, n, k):
    index_dict = {0:-1}
    prefix_sum = 0
    max_len = 0
    for i in range(n):
        prefix_sum+=arr[i]
        curr_sum = prefix_sum - k
        if index_dict.get(curr_sum)!=None:
            curr_len = i - index_dict[curr_sum] 
            max_len = max(max_len, curr_len)
        else:
            index_dict[prefix_sum] = i
    return max_len

'''
Problem : https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
TC - O(n)
SC - O(n)
Approach:
This problem is similar to Largest subarray sum 0, 
But in this we look for the if prefixsum-target is already present in array or  not.
'''