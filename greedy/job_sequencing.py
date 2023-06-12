from typing import List
from functools import cmp_to_key

def comparator(a1,a2):
    if a1[0]>a2[0]:
        return -1
    elif a1[0]==a2[0]:
        if a1[1]<a2[1]:
            return -1
    return 1


def jobSequencing(n: int, deadline: List[int], profit: List[int]) -> int:
    max_deadline = 0
    jobs = []
    max_profit = 0

    for i in range(n):
        jobs.append((profit[i],deadline[i]))
        max_deadline = max(max_deadline,deadline[i])
    
    jobs = sorted(jobs, key=cmp_to_key(comparator))

    deadlines = [0]*(max_deadline+1)

    for i in range(n):
        deadline = jobs[i][1]

        while deadlines[deadline]!=0 and deadline>0:
            deadline-=1

        if deadline>0:
            deadlines[deadline] = jobs[i][0]
            max_profit+=jobs[i][0]
    
    return max_profit




def main():
    n = int(input())
    deadline = input().strip().split(' ')
    profit = input().strip().split(' ')
    deadline = [int(x) for x in deadline]
    profit = [int(x) for x in profit]
    print(jobSequencing(n,deadline,profit))

if __name__=="__main__":
    main()

'''
Approach :
1.Create a list of jobs, where each job is represented by a tuple containing its profit and deadline.
2.Sort the jobs list in descending order of profits, and in case of a tie, sort by increasing order of deadlines.
3.Initialize the maximum deadline as 0 and the maximum profit as 0.
4.Iterate over each job in the sorted jobs list.
5.For each job, find the next available slot for its deadline by decrementing the deadline until an unoccupied slot is found.
6.If an unoccupied slot is found (deadline > 0), assign the job to that slot by updating the corresponding entry in the deadlines list with the job's profit.
7.Increment the maximum profit by the job's profit.
8.Finally, return the maximum profit as the result.

'''