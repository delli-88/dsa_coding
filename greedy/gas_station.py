from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = 0
        sum_cost = 0
        gas_available = 0
        start = 0
        
        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            gas_available += gas[i] - cost[i]
            
            if gas_available < 0:
                start = i + 1
                gas_available = 0
        
        if sum_cost > sum_gas:
            return -1
        else:
            return start





print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))

'''
Problem : https://leetcode.com/problems/gas-station/
TC - O(n)
SC - O(1)
Approach :
1.Calculate the total gas and total cost by summing up the corresponding values from the gas and cost lists.
2.If the total cost is greater than the total gas, it is impossible to complete the circuit, so return -1.
3.Initialize the gas_available variable to 0. This variable represents the gas available at the current position.
4.Initialize the start variable to 0. This variable represents the potential starting position of the circuit.
5.Iterate over the gas stations from 0 to n-1:
    5a.Increment the sum_gas variable by adding the current gas station's gas value.
    5b.Increment the sum_cost variable by adding the current gas station's cost value.
    5c.Calculate the gas available at the current position by subtracting the cost from the gas.
    5d.If the gas available is negative, it means we cannot reach the next gas station from the current position. So, update the start variable to the next position (i+1) and reset the gas_available to 0.
6.After the loop, check if the total cost is greater than the total gas. If it is, return -1 because it is impossible to complete the circuit.
7.Otherwise, return the start position as it represents the starting point of the circuit.
'''