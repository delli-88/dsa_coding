from math import inf
def multiply(num, x,n):
    ans = 1
    
    while n>0:
        if n%2!=0:
            ans = ans*num
        n = n//2
        if num>x or ans>x:
            ans = inf
            break
        num = num * num
    return ans

def nthRoot(x: int, n: int) -> int:

    start = 1
    end = x
    min_start = 0

    while start<=end:

        mid = (start+end)//2

        nth_root = multiply(mid,x,n)
        if nth_root<=x:
            min_start = mid
            start = mid+1
        else:
            end = mid-1

    return min_start




def main():
    test = int(input())
    output = ""
    for t in range(test):
        x, n = list(map(int, input().split()))
        result = nthRoot(x, n)
        output += str(result) + "\n"
    print(output)

if __name__=="__main__":
    main()




'''
Problem : https://www.geeksforgeeks.org/n-th-root-number/
TC : O(logn)
SC : O(1)
Approach:
We follow binary search here
Our search space will be from 1 to x
we calc mid, and if mid power n is greater than x, we continue search left of mid
else we continue search right of mid
'''