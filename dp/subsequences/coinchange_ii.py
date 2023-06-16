# DP - Tabulation - Space Optimization
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0 for _ in range(amount+1)]

        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i] = 1
        prev[0] = 1

        for i in range(1,len(coins)):
            temp = [0 for _ in range(amount+1)]
            temp[0] = 1
            for j in range(1,amount+1):
                take = 0
                if (coins[i]<=j):
                    take = temp[j-coins[i]]
                no_take = prev[j]
                temp[j] =  take + no_take
            prev = temp
        print(prev)
        return prev[-1]

'''
Problem : https://leetcode.com/problems/coin-change-ii/
TC - O(coins*amount)
SC - O(amount)
Approach :
1.Create an array prev of size amount + 1 initialized with zeros. This array will store the number of combinations for each amount from 0 to amount.
2.Iterate over the range of amount + 1 and check if each amount is divisible by the first coin coins[0]. If it is, set prev[i] to 1 since there is one possible combination for that amount.
3.Set prev[0] to 1 to indicate that there is one possible combination to make an amount of 0 (by not selecting any coin).
4.Iterate over the range of 1 to the length of coins (excluding the first coin):
    a.Create a temporary array temp of size amount + 1 initialized with zeros. This array will store the updated number of combinations for each amount.
    b.Set temp[0] to 1 to indicate that there is one possible combination to make an amount of 0 (by not selecting any coin).
    c.Iterate over the range of 1 to amount + 1 (excluding 0):
        i.Calculate the number of combinations take if the current coin coins[i] is taken. This is done by accessing the value in temp at index j - coins[i]. If coins[i] is less than or equal to j, it means we can take the current coin and consider the remaining amount j - coins[i] to form the combinations.
        ii.Calculate the number of combinations no_take if the current coin is not taken. This is done by accessing the value in prev at index j. Since we are not taking the current coin, the number of combinations remains the same as in the previous iteration.
        iii.Update temp[j] by adding take and no_take, representing the total number of combinations for the current amount j.
    d.Update prev to be the same as temp for the next iteration.
5.Return the last element of prev, which represents the total number of combinations to make the given amount using the given coins.
'''

'''
# DP - Tabulation
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i] = 1
            
        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(1,len(coins)):
            for j in range(amount+1):
                take = 0
                if (coins[i]<=j):
                    take = dp[i][j-coins[i]]
                no_take = dp[i-1][j]
                dp[i][j] =  take + no_take

        return dp[-1][-1]
'''
                
'''
TC - O(coins*amount)
SC - O(coins*amount)
Approach :
1.Create a 2D DP (dynamic programming) array, dp, of size len(coins) by amount+1. Each element dp[i][j] represents the number of combinations to make the amount j using the first i+1 coins.
2.Initialize the base cases:
    a.Set dp[0][j] = 1 for each j where j is a multiple of coins[0]. This is because if the amount is a multiple of the first coin, we can use only the first coin to make that amount, so there is only one combination possible.
    b.Set dp[i][0] = 1 for each i representing the first i+1 coins. This is because we can always make the amount 0 by not selecting any coins.
3.Iterate through the remaining coins starting from the second coin (i = 1) up to the last coin (i = len(coins) - 1):
    a.For each coin coins[i], iterate through the amounts j from 1 to amount.
    b.For each amount j:
        I.Check if the current coin can be used to make the amount (coins[i] <= j):
            i.If yes, set take as dp[i][j-coins[i]], which represents the number of combinations to make the remaining amount after considering the current coin.
            ii.If no, set take as 0 since the current coin cannot be used to make the amount j.
        II.Set no_take as dp[i-1][j], which represents the number of combinations without considering the current coin.
        III.Set dp[i][j] as the sum of take and no_take, indicating the total number of combinations to make the amount j using the first i+1 coins.
4.Finally, return the value at dp[-1][-1], which represents the number of combinations to make the total amount using all the coins
'''

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
