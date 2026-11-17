"""Compare greedy job sequencing with brute force on random instances."""
import itertools, random
from job_sequencing import job_sequencing


def feasible(subset):
    # a set is feasible iff, sorted by deadline, the k-th job has deadline >= k
    return all(j[1] >= k + 1 for k, j in enumerate(sorted(subset, key=lambda j: j[1])))


def brute(jobs):
    best = 0
    for r in range(len(jobs) + 1):
        for c in itertools.combinations(jobs, r):
            if feasible(c):
                best = max(best, sum(j[2] for j in c))
    return best


random.seed(4)
for t in range(500):
    n = random.randint(1, 8)
    jobs = [(f"J{i}", random.randint(1, n), random.randint(1, 100)) for i in range(n)]
    g = job_sequencing(jobs, verbose=False)[1]
    assert g == brute(jobs), (jobs, g, brute(jobs))
print("PASS: greedy == brute force on 500 random instances")
