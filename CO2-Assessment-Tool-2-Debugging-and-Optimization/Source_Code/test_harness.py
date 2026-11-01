
import math

from original_debugged import (
    sort_alerts,
    is_blocked,
    find_signature,
    closest_logins
)

from sentinelops_optimized import (
    create_blocked_set,
    is_blocked as fast_is_blocked,
    closest_logins_brute,
    closest_logins_optimized
)


def run_tests():

    print("SENTINELOPS TEST HARNESS")
    print("------------------------")

    # Alert sorting
    alerts = [
        ("A1", 3),
        ("A2", 9),
        ("A3", 5),
        ("A4", 9),
        ("A5", 1)
    ]

    expected = [
        ("A2", 9),
        ("A4", 9),
        ("A3", 5),
        ("A1", 3),
        ("A5", 1)
    ]

    assert sort_alerts(alerts.copy()) == expected
    print("Alert sorting: PASS")

    # IP blocklist
    blocklist = [
        "10.0.0.5",
        "10.0.0.9",
        "172.16.4.2"
    ]

    assert is_blocked(blocklist, "10.0.0.9") is True
    assert is_blocked(blocklist, "8.8.8.8") is False
    assert is_blocked([], "8.8.8.8") is False

    blocked_set = create_blocked_set(blocklist)

    assert fast_is_blocked(blocked_set, "10.0.0.5") is True
    assert fast_is_blocked(blocked_set, "8.8.8.8") is False

    print("IP blocklist: PASS")

    # Signature matching
    assert find_signature("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert find_signature("ABCFAIL", "FAIL") == [3]
    assert find_signature("ABC", "LONGPATTERN") == []
    assert find_signature("ABC", "") == []
    assert find_signature("AAAA", "AA") == [0, 1, 2]

    print("Signature matching: PASS")

    # Closest pair
    events = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]

    pair, distance = closest_logins(events)

    assert abs(distance - math.sqrt(2)) < 0.000001

    pair1, distance1, _ = closest_logins_brute(events)
    pair2, distance2, _ = closest_logins_optimized(events)

    assert abs(distance1 - distance2) < 0.000001

    assert closest_logins([])[0] is None
    assert closest_logins([(1, 2)])[0] is None

    print("Closest pair: PASS")
    print("Boundary cases: PASS")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_tests()

