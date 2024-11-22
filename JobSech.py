class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)  # Sort jobs by profit in descending order
    result = [False] * n  # Track whether a time slot is filled
    job_sequence = [None] * n  # Track the job sequence for each time slot

    for job in jobs:
        # Find a time slot from job's deadline backwards
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not result[j]:  # If the time slot is free
                result[j] = True
                job_sequence[j] = job.job_id  # Assign job to this slot
                break

    # Filter out None values and get scheduled jobs
    scheduled_jobs = [job for job in job_sequence if job is not None]
    return scheduled_jobs

def take_input():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        print(f"Enter details for job {i+1}:")
        job_id = input("Job ID: ")
        profit = int(input("Profit: "))
        deadline = int(input("Deadline: "))
        jobs.append(Job(job_id, profit, deadline))
    return jobs, n

if __name__ == "__main__":
    jobs, n = take_input()
    max_jobs = job_scheduling(jobs, n)
    print("Scheduled jobs for maximum profit:", max_jobs)
