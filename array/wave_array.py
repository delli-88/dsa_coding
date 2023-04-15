from typing import List
def wiggleSort(nums: List[int]) -> List[int]:

    for i in range(1,len(nums),2):
        if i==len(nums)-1:
            if nums[i]<nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        else:
            if nums[i]<nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            
            if nums[i]<nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


'''
Problem : https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1
TC - O(n)
SC - O(1)
Optimal Approach :
We notice in our question, that only the elements at odd positions have to be larger than both their neighbors.
we traverse through the array - considering only odd position elements.
    If a[i], where i is odd, is less than a[i-1], we swap the two.
    If a[i] is less than a[i+1], we swap them as well.
repeated for all elements in odd positions.
When we reach the end of the array, we'll have every element at odd positions being larger than both its neighbors, which is exactly what we want.
'''

'''
def wiggleSort(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    mid = len(nums)//2
    i = 0
    if n%2==0:
        j = mid
    else:
        j = mid+1
    sol = [0]*len(nums)
    k = 0
    while j<n:
        if k%2==0:
            sol[k] = nums[i]
            i+=1
        else:
            sol[k] = nums[j]
            j+=1
        k+=1
    if k<n:
        sol[k] = nums[i]
        i+=1
        k+=1
    return sol
Approach :
We sort the array,
We can take two pointers, i from 0, j from mid
We loop for n times
    on even index, we take i, 
    on odd we take j
    append to new sol
resturn sol
TC - O(nlogn)
SC - (n)
'''

'''
def main():
    n = int(input().strip())
    nums = list(map(int,input().strip().split()))

    ans = wiggleSort(nums)
    print(*ans)

if __name__=="__main__":
    main()
'''