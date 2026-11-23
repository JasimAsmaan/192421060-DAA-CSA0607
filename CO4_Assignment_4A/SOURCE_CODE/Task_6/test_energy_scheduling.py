"""Compare DP with brute force on random instances; show greedy failures."""
import random
from energy_scheduling import schedule, brute_force, greedy_earliest_finish, greedy_max_value

random.seed(5)
ge = gv = 0
for t in range(1000):
    n = random.randint(1, 8)
    jobs = []
    for i in range(n):
        s = random.randint(0, 12)
        jobs.append((f"J{i}", s, s + random.randint(1, 6), random.randint(1, 60)))
    best, sel, _ = schedule(jobs)
    assert best == brute_force(jobs)[0], jobs
    d = {j[0]: j for j in jobs}
    sel_jobs = sorted((d[x] for x in sel), key=lambda j: j[1])
    assert all(sel_jobs[k][2] <= sel_jobs[k + 1][1] for k in range(len(sel_jobs) - 1))
    ge += greedy_earliest_finish(jobs)[0] < best
    gv += greedy_max_value(jobs)[0] < best
print("PASS: DP == brute force (value and feasibility) on 1000 random instances")
print(f"Earliest-finish greedy was suboptimal in {ge}/1000 cases")
print(f"Highest-value greedy was suboptimal in {gv}/1000 cases")
