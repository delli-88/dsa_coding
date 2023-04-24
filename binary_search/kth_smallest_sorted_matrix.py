from typing import List
class Solution:
    def rank(self,num, mat):
        
        sqmt_len = len(mat)
        count = 0
        req_col_ind = 0
        for i in range(sqmt_len):
            if mat[i][0]<=num and mat[i][sqmt_len-1]<=num:
                count+=sqmt_len
            elif mat[i][0]<=num and mat[i][sqmt_len-1]>=num:
                col_start = 0
                col_end = sqmt_len-1
                while col_start<=col_end:
                    col_mid = (col_start+col_end)//2
                    if mat[i][col_mid]<=num:
                        req_col_ind=col_mid
                        col_start = col_mid+1
                    else:
                        col_end= col_mid-1      
                count += req_col_ind+1    
            elif mat[i][0]>num:
                break
        
        return count



    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sqmt_len = len(matrix)
        start = matrix[0][0]
        end = matrix[sqmt_len-1][sqmt_len-1]
        kth_smallest = 0


        while start<=end:
            mid = (start+end)//2

            if self.rank(mid,matrix)>=k:
                kth_smallest = mid
                end = mid-1
            else:
                start = mid+1
        return kth_smallest

'''
Problem:https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Approach :
We follow binary search here
our search space will be mat start element and mat end element as mat is sorted row & col wise
at mid we find the rank of mid(rank is num of elements lesthan or equal to that curr number)
if rank is less, that means we haven't fonund k smaller elements yet, so we continue searching to right of mid
but if we found rank is less than or equal to mid, we store that and continue searching to left of mid(
we do this step because we are not sure that the curr mid is present in the array or not, so we store it and keep searching
if the curr mid is not in matrix, as we move left we still should see the rank to be same next time
)
we return the kth_smallest

'''
print(Solution().kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))

