"""Task 2 - Job Sequencing with Deadlines (greedy).

Greedy-choice rule: consider jobs in descending order of profit; place each job
in the LATEST free slot on or before its deadline; skip it if none is free.
"""


def job_sequencing(jobs, verbose=True):
    """jobs: list of (id, deadline, profit). Returns (schedule, total_profit)."""
    jobs_sorted = sorted(jobs, key=lambda j: j[2], reverse=True)
    max_deadline = max(j[1] for j in jobs)
    slot = [None] * (max_deadline + 1)   # slot[1..max_deadline]; index 0 unused
    total = 0

    if verbose:
        print("Sorted by profit:", [(j[0], j[1], j[2]) for j in jobs_sorted])
    for jid, d, p in jobs_sorted:
        placed = False
        for t in range(d, 0, -1):        # latest free slot <= deadline
            if slot[t] is None:
                slot[t] = jid
                total += p
                placed = True
                if verbose:
                    print(f"  Job {jid} (d={d}, p={p}) -> slot {t}   | slots={slot[1:]} total={total}")
                break
        if not placed and verbose:
            print(f"  Job {jid} (d={d}, p={p}) REJECTED (no free slot <= {d}) | slots={slot[1:]} total={total}")
    return slot[1:], total


if __name__ == "__main__":
    jobs = [("A", 2, 80), ("B", 1, 35), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    print("=== Task 2.4 desk-check instance ===")
    sched, total = job_sequencing(jobs)
    print("Final schedule (slot1..slotN):", sched)
    print("Total profit:", total)

    print("\n=== Task 2.5 challenge: change B profit 35 -> 70 ===")
    jobs2 = [("A", 2, 80), ("B", 1, 70), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    sched2, total2 = job_sequencing(jobs2)
    print("Final schedule (slot1..slotN):", sched2)
    print("Total profit:", total2)
