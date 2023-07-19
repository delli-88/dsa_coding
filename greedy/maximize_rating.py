'''
Problem Statement: Maximizing Rating with Weapons Usage and Selling
You are given an initial power P, a starting rating of 0, and a suitcase of weapons, where each weapon has a certain power value (weapon[i]). Your objective is to maximize your total rating by using each weapon in one of two ways:
Weapon Usage: You may utilize the i-th weapon if your current power is at least weapon[i]. By using the i-th weapon, you will lose weapon[i] power and gain 1 rating.
Weapon Selling: If you have a higher rating than 0, you can sell the i-th weapon. By selling the i-th weapon, you will gain weapon[i] power and lose 1 rating.
Each weapon may be used at most once and in any order. Your task is to find the maximum possible rating you can achieve after using any number of weapons.
'''

def weapons(n, P, weapon):

    weapon.sort()
    left, right = 0, n - 1
    rating = 0
    power = P
    maxi = 0

    while left<=right:
        if power>=weapon[left]:
            power-=weapon[left]
            rating+=1
            left+=1
            maxi = max(maxi, rating)
        else:
            power+=weapon[right]
            rating-=1
            right-=1

    return maxi

# Test cases
print(weapons(4, 6, [2, 1, 3, 1]))  # Output: 3
print(weapons(5, 10, [2, 1, 3, 1, 2]))  # Output: 5t
print(weapons(4,2,[3,2,5,1]))
print(weapons(5,8,[1,2,3,4,5]))


'''
Approach : Greedy

1.Sort the list of weapons in ascending order. Sorting is required to apply the two-pointer approach effectively.
2.Initialize two pointers, left and right, to the start and end of the sorted weapons list, respectively.
3.Initialize two variables, rating and power, to 0 and the given initial power P, respectively. The rating will keep track of the current rating, and the power will keep track of the remaining power.
4.Initialize a variable max_rating to 0. This variable will store the maximum rating achieved during the process.
5.Use a while loop with the condition left <= right, which means there are still weapons available to consider.
6.Inside the loop, check if the power is greater than or equal to the power value of the weapon at the left index. If it is, it means you have enough power to use this weapon. In this case, do the following:
    a.Subtract the power value of the weapon at the left index from the power.
    b.Increment the rating by 1 (as you are using this weapon, you gain 1 rating).
    c.Move the left pointer one step ahead.
7.If the power is less than the power value of the weapon at the left index, it means you cannot use this weapon without sacrificing your current rating. In this case, do the following:
    a.Add the power value of the weapon at the right index to the power.
    b.Decrement the rating by 1 (as you are selling this weapon, you lose 1 rating).
    c.Move the right pointer one step back.
8.After each iteration, update the max_rating with the maximum value between the current rating and the max_rating.
9.Finally, when the loop finishes, return the max_rating.


TC - O(nlogn)
SC - O(1)
'''