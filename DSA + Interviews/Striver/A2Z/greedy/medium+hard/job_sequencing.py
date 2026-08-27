"""
Problem Statement: You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

Example 1:
Input:

N = 4, Jobs = {(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)}
Output:
 2 60
Explanation:

- The 3rd job with a deadline of 1 is performed during the first unit of time.
- The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60.
So, the result is 2 jobs with a total profit of 60.

Example 2:
Input:

N = 5, Jobs = {(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)}
Output:
 2 127
Explanation:

The first and third jobs, both having a deadline of 2, give the highest profit.
Profit = 100 + 27 = 127.
So, the result is 2 jobs with a total profit of 127.

OPTIMAL:
- sort by profit, and then try to fill each slot up to the max deadline with the best one available
"""
N = 4
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]

def func(N, jobs):
    job_count = 0
    filled = [-1] * max(job[1] for job in jobs)

    jobs.sort(key=lambda x: x[2], reverse=True)

    for i in range(len(jobs)):
        id, deadline, amt = jobs[i]

        for j in range(len(filled) - 1, -1, -1):
            if deadline >= j + 1 and filled[j] == -1:
                filled[j] = amt
                job_count += 1
                break

        print(filled)

    profit = sum(amount for amount in filled if amount != -1)

    return job_count, profit

print(func(N, jobs))