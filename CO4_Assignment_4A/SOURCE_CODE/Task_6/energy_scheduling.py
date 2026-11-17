"""Task 6 - Energy-Aware Job Scheduling = Weighted Interval Scheduling (DP).

State: OPT[i] = max energy-saving using only the first i jobs (sorted by finish time).
p(i)  = largest index j < i whose finish time <= start time of job i (0 if none).
Recurrence: OPT[i] = max(OPT[i-1], value[i] + OPT[p(i)]);  OPT[0] = 0.
"""
import bisect
import itertools


def schedule(jobs):
    """jobs: list of (id, start, finish, value). Returns (best, selected_ids, trace)."""
    jobs = sorted(jobs, key=lambda j: j[2])              # sort by finish time
    n = len(jobs)
    finishes = [j[2] for j in jobs]
    # p[i] for 1-based i: number of jobs with finish <= start_i (those are indices 1..p)
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = bisect.bisect_right(finishes, jobs[i - 1][1], 0, i - 1)

    OPT = [0] * (n + 1)
    take = [False] * (n + 1)
    trace = []
    for i in range(1, n + 1):
        jid, s, f, v = jobs[i - 1]
        incl = v + OPT[p[i]]
        excl = OPT[i - 1]
        if incl > excl:
            OPT[i], take[i] = incl, True
        else:
            OPT[i] = excl
        trace.append((jid, s, f, v, p[i], incl, excl, OPT[i], "INCLUDE" if take[i] else "EXCLUDE"))

    selected, i = [], n                                  # reconstruction
    while i > 0:
        if take[i]:
            selected.append(jobs[i - 1][0])
            i = p[i]
        else:
            i -= 1
    selected.reverse()
    return OPT[n], selected, trace


def brute_force(jobs):
    best, best_set = 0, []
    for r in range(len(jobs) + 1):
        for combo in itertools.combinations(jobs, r):
            c = sorted(combo, key=lambda j: j[1])
            if all(c[k][2] <= c[k + 1][1] for k in range(len(c) - 1)):
                val = sum(j[3] for j in c)
                if val > best:
                    best, best_set = val, [j[0] for j in c]
    return best, best_set


def greedy_earliest_finish(jobs):
    jobs = sorted(jobs, key=lambda j: j[2])
    sel, last, tot = [], -1, 0
    for jid, s, f, v in jobs:
        if s >= last:
            sel.append(jid); last = f; tot += v
    return tot, sel


def greedy_max_value(jobs):
    jobs = sorted(jobs, key=lambda j: j[3], reverse=True)
    sel, tot = [], 0
    for jid, s, f, v in jobs:
        if all(f <= s2 or f2 <= s for _, s2, f2, _ in sel):
            sel.append((jid, s, f, v)); tot += v
    return tot, [x[0] for x in sel]


if __name__ == "__main__":
    JOBS = [("J1", 1, 3, 20), ("J2", 2, 5, 50), ("J3", 4, 6, 30), ("J4", 6, 8, 40),
            ("J5", 5, 9, 60), ("J6", 8, 10, 30), ("J7", 9, 11, 50), ("J8", 11, 13, 40)]
    print("=== Stage 5: DP on the 8-job dataset ===")
    best, sel, trace = schedule(JOBS)
    print(f"{'Job':<4}{'s':>3}{'f':>4}{'v':>4}{'p(i)':>6}{'include':>9}{'exclude':>9}{'OPT':>5}  decision")
    for t in trace:
        print(f"{t[0]:<4}{t[1]:>3}{t[2]:>4}{t[3]:>4}{t[4]:>6}{t[5]:>9}{t[6]:>9}{t[7]:>5}  {t[8]}")
    print("Selected jobs:", sel)
    print("Maximum energy saving:", best)
    print("Brute-force check:", brute_force(JOBS))
    print("Greedy earliest-finish (unweighted) gives:", greedy_earliest_finish(JOBS))
    print("Greedy highest-value gives:", greedy_max_value(JOBS))

    print("\n=== Stage 6: adversarial dataset ===")
    ADV = [("X1", 0, 4, 10), ("X2", 4, 8, 10), ("X3", 8, 12, 10),
           ("X4", 0, 12, 100), ("X5", 3, 9, 15)]
    print("Jobs:", ADV)
    print("Greedy earliest-finish:", greedy_earliest_finish(ADV))
    print("Greedy highest-value  :", greedy_max_value(ADV))
    best, sel, trace = schedule(ADV)
    for t in trace:
        print(f"  {t[0]} s={t[1]} f={t[2]} v={t[3]} p={t[4]} incl={t[5]} excl={t[6]} OPT={t[7]} {t[8]}")
    print("DP result:", best, sel)
    print("Brute force:", brute_force(ADV))

    ADV2 = [("Y1", 0, 5, 10), ("Y2", 4, 9, 11), ("Y3", 8, 13, 10), ("Y4", 0, 13, 25), ("Y5", 5, 8, 8)]
    print("\nSecond adversarial set:", ADV2)
    print("Greedy earliest-finish:", greedy_earliest_finish(ADV2))
    print("Greedy highest-value  :", greedy_max_value(ADV2))
    print("DP result:", schedule(ADV2)[:2])
    print("Brute force:", brute_force(ADV2))
