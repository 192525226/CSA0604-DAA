n = int(input("Enter number of jobs: "))

jobs = []

print("Enter deadline and profit for each job:")

for i in range(n):
    deadline, profit = map(int, input().split())
    jobs.append((deadline, profit, i + 1))

jobs.sort(key=lambda x: x[1], reverse=True)

max_deadline = max(job[0] for job in jobs)

slots = [-1] * max_deadline
total_profit = 0

for deadline, profit, job_id in jobs:
    for j in range(min(max_deadline, deadline) - 1, -1, -1):
        if slots[j] == -1:
            slots[j] = job_id
            total_profit += profit
            break

print("Selected jobs:", [x for x in slots if x != -1])
print("Maximum profit:", total_profit)