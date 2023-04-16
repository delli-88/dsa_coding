class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # ori = n
        array_num = []
        while n>0:
            array_num.append(n%10)
            n = n // 10
        array_num = array_num[::-1]
        ele_index = -1
        n = len(array_num)
        for i in range(n-1,0,-1):
            if array_num[i]>array_num[i-1]:
                ele_index_to_be = i
                ele_index = i-1
                break
        if ele_index==-1:
                    return ele_index
        for j in range(i,n):
            if array_num[j]>array_num[ele_index] and array_num[j]<=array_num[ele_index_to_be]:
                ele_index_to_be = j
        array_num[ele_index],array_num[ele_index_to_be] = array_num[ele_index_to_be], array_num[ele_index]

        array_num = array_num[:ele_index+1] + array_num[n-1:ele_index:-1]
        array_num = array_num[::-1]

        num = 0
        for j in range(n-1, -1, -1):
            num =  10*num + array_num[j]

        if  num<-2147483648 or num>2147483647:
            return -1
        return num

'''
Problem : https://leetcode.com/problems/next-greater-element-iii/
TC - O(n)
SC - O(n) (for storing number in array)/ O(1)
Optimal Approach:
Convert input the number to an array of digits
if num is in descending order, we return -1
We traverse the array from end
    starting from the last digit of number find a digit which is smaller than the just previous one.
We traverse from the index of the ele we found to n
    This smaller digit is now swapped with a number which is just greater than this digit but not the largest one
Finally, reverse the digits present next to this number in ascending order
'''

print(Solution().nextGreaterElement(12222333))

