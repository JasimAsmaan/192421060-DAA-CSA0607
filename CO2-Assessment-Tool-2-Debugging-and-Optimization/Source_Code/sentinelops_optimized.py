
import math


def sort_alerts(alerts):
    """Sort alerts by descending severity while preserving equal-severity order."""
    return sorted(alerts, key=lambda alert: alert[1], reverse=True)


def create_blocked_set(blocklist):
    """Create a reusable set for repeated IP lookups."""
    return set(blocklist)


def is_blocked(blocked_set, ip):
    """Check blocklist membership using average O(1) set lookup."""
    return ip in blocked_set


def find_signature(log, pattern):
    """Find all pattern occurrences using brute-force matching."""
    n = len(log)
    m = len(pattern)
    hits = []

    if m == 0:
        return hits

    for i in range(n - m + 1):
        j = 0

        while j < m and log[i + j] == pattern[j]:
            j += 1

        if j == m:
            hits.append(i)

    return hits


def closest_logins_brute(events):
    """Calculate the closest pair using all distinct pairs."""
    if len(events) < 2:
        return None, float("inf"), 0

    min_dist_sq = float("inf")
    pair = None
    count = 0

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            distance_sq = dx * dx + dy * dy
            count += 1

            if distance_sq < min_dist_sq:
                min_dist_sq = distance_sq
                pair = (events[i], events[j])

    return pair, math.sqrt(min_dist_sq), count


def closest_logins_optimized(events):
    """Find the closest pair using x-coordinate pruning."""
    if len(events) < 2:
        return None, float("inf"), 0

    points = sorted(events, key=lambda point: point[0])

    min_dist_sq = float("inf")
    pair = None
    count = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dx = points[j][0] - points[i][0]

            if dx * dx >= min_dist_sq:
                break

            dy = points[j][1] - points[i][1]
            distance_sq = dx * dx + dy * dy
            count += 1

            if distance_sq < min_dist_sq:
                min_dist_sq = distance_sq
                pair = (points[i], points[j])

    return pair, math.sqrt(min_dist_sq), count


if __name__ == "__main__":

    alerts = [
        ("A1", 3),
        ("A2", 9),
        ("A3", 5),
        ("A4", 9),
        ("A5", 1)
    ]

    blocklist = [
        "10.0.0.5",
        "10.0.0.9",
        "172.16.4.2"
    ]

    queries = [
        "10.0.0.9",
        "10.0.0.5",
        "8.8.8.8"
    ]

    log = "FAILFAIXFAIL"
    pattern = "FAIL"

    events = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]

    print("OPTIMISED SENTINELOPS MODULE")

    print("\nSORTED ALERTS:")
    print(sort_alerts(alerts))

    blocked_set = create_blocked_set(blocklist)

    print("\nIP BLOCKLIST RESULTS:")
    for ip in queries:
        print(ip, "->", is_blocked(blocked_set, ip))

    print("\nSIGNATURE SEARCH:")
    print(find_signature(log, pattern))

    pair, distance, count = closest_logins_optimized(events)

    print("\nOPTIMISED CLOSEST PAIR:")
    print("Closest Pair:", pair)
    print("Minimum Distance:", round(distance, 4), "km")
    print("Distance Comparisons:", count)

