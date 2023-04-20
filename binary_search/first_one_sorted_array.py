from typing import List

def zeroOnes(n: int, arr: List[int]) -> int:
  start = 0
  end = n-1

  while start<=end:
    mid = (start+end)//2
   
    if arr[mid]==0: 
      start = mid+1
    else:
      if arr[mid-1]==0 or mid==0:
        return mid
      elif arr[mid-1]==1:
        end = mid-1
        
  return -1

'''
Problem : https://www.geeksforgeeks.org/find-index-first-1-sorted-array-0s-1s/
TC - O(logn)
SC - O(1)
Approach :  
We make use of the fact that the array is sorted, which means that we can apply binary search.
The first 1 will have a 0 before it.
Therefore, we are searching for an A[i] = 1, such that A[i-1] = 0.
The binary search function can be modified to look for such an element.
'''