
import math


def sort_alerts(alerts):
    """Sort alerts by severity using stable insertion sort."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1

        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1

        alerts[j + 1] = key

    return alerts


def is_blocked(blocklist, ip):
    """Check an IP address using sequential search."""
    for address in blocklist:
        if address == ip:
            return True

    return False


def find_signature(log, pattern):
    """Find all occurrences using brute-force string matching."""
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


def closest_logins(events):
    """Find the closest pair using brute-force comparison."""
    if len(events) < 2:
        return None, float("inf")

    min_dist = float("inf")
    pair = None

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            distance = math.sqrt(dx * dx + dy * dy)

            if distance < min_dist:
                min_dist = distance
                pair = (events[i], events[j])

    return pair, min_dist


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

    print("SORTED ALERTS:")
    print(sort_alerts(alerts))

    print("\nIP BLOCKLIST RESULTS:")
    for ip in queries:
        print(ip, "->", is_blocked(blocklist, ip))

    print("\nSIGNATURE SEARCH:")
    print(find_signature(log, pattern))

    print("\nCLOSEST LOGIN LOCATIONS:")
    pair, distance = closest_logins(events)
    print("Closest Pair:", pair)
    print("Minimum Distance:", round(distance, 4), "km")

