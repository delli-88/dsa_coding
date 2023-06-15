# DP - Tabulation
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            for j in range(amount+1):
                pass

        

# TC - O(coins*amount)
# SC - O(coins*amount) + O(amount)
# Approach :

'''
# DP - Memoization
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        return self.changeHelper(amount,coins,0, dp)

    def changeHelper(self,amount, coins, pos, dp):
        if amount<0 or pos>=len(coins):
            return 0
        if amount==0:
            return 1

        if dp[pos][amount]!=-1:
            return dp[pos][amount]

        pick = self.changeHelper(amount-coins[pos], coins, pos, dp)
        no_pick = self.changeHelper(amount, coins, pos+1, dp)

        dp[pos][amount] = pick+no_pick

        return dp[pos][amount]

# TC - O(coins*amount)
# SC - O(coins*amount) + O(amount)
# Approach :
1.Initialize the dp table with -1 for all cells.
2.Call changeHelper with the initial amount, coins, pos=0, and the dp table.
3.Inside changeHelper:
    a.If amount is less than 0 or pos is out of range, return 0 (as it is not a valid combination).
    b.If amount is 0, return 1 (as it is a valid combination).
    c.If the result for the current pos and amount is already computed (stored in dp), return the stored result.
    d.Recursively call changeHelper with two scenarios:
        i.Picking the coin at pos and subtracting its value from amount.
        ii.Not picking the coin at pos and moving to the next coin.
4.Compute the sum of the above two scenarios and store it in the dp table.
5.Return the stored result for the current pos and amount.
'''

'''
# Recursion
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = [0]
        self.changeHelper(amount,coins,0,count)
        return count[0]

    def changeHelper(self,amount, coins, pos, count):
        if amount<0 or pos>=len(coins):
            return
        if amount==0:
            count[0]+=1
            return

        self.changeHelper(amount-coins[pos], coins, pos, count)
        self.changeHelper(amount, coins, pos+1, count)

        return

TC - O(2^n)
SC - O(n)
Approach :
1.Initialize a count variable as a list containing a single element, count = [0]. This variable will store the count of valid combinations.
2.Call the changeHelper function with the initial amount, coins list, starting position 0, and the count variable.
3.In the changeHelper function:
    3a.Check for base cases:
        i.If the amount becomes negative or the position goes beyond the length of the coins list, return.
        ii.If the amount becomes 0, increment the count by 1 and return.
    3b.Recursively call the changeHelper function with two scenarios:
        i.Subtract the current coin from the amount and call the function with the same position. This represents using the current coin in the combination.
        ii.Call the function with the next position without subtracting the current coin. This represents excluding the current coin from the combination.
4.Finally, return the value stored in count[0] as the total number of combinations.
'''



print(Solution().change(amount = 5, coins = [1,2,5]))