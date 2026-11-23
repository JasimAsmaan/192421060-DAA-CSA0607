
# Pseudocode – SentinelOps SOC Alert-Triage Module

## 1. Alert Sorting – Insertion Sort

### Aim
Sort alerts by severity in descending order while maintaining the arrival order of alerts with equal severity.

### Pseudocode

```text
SORT_ALERTS(alerts)

1. FOR i = 1 TO length(alerts) - 1
2.     key = alerts[i]
3.     j = i - 1
4.     WHILE j >= 0 AND alerts[j].severity < key.severity
5.         alerts[j + 1] = alerts[j]
6.         j = j - 1
7.     END WHILE
8.     alerts[j + 1] = key
9. END FOR
10. RETURN alerts
```

Time Complexity:
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

Space Complexity: O(1)

## 2. IP Blocklist – Sequential Search

### Aim
Check whether a source IP address exists in the blocklist.

### Pseudocode

```text
IS_BLOCKED(blocklist, ip)

1. FOR each address in blocklist
2.     IF address == ip
3.         RETURN TRUE
4.     END IF
5. END FOR
6. RETURN FALSE
```

Time Complexity:
- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity: O(1)

## 3. Optimised IP Blocklist – Set Lookup

### Aim
Improve repeated IP address lookups using a hash set.

### Pseudocode

```text
CREATE_BLOCKED_SET(blocklist)

1. blocked_set = CONVERT blocklist INTO SET
2. RETURN blocked_set

IS_BLOCKED_FAST(blocked_set, ip)

1. IF ip EXISTS IN blocked_set
2.     RETURN TRUE
3. ELSE
4.     RETURN FALSE
5. END IF
```

Average Time Complexity: O(1) per lookup after set construction.

Space Complexity: O(n)

## 4. Attack Signature – Brute-Force String Matching

### Aim
Find all occurrences of a pattern in a given log message.

### Pseudocode

```text
FIND_SIGNATURE(log, pattern)

1. n = length(log)
2. m = length(pattern)
3. hits = empty list

4. IF m == 0
5.     RETURN hits
6. END IF

7. FOR i = 0 TO n - m
8.     j = 0
9.     WHILE j < m AND log[i + j] == pattern[j]
10.        j = j + 1
11.    END WHILE

12.    IF j == m
13.        ADD i TO hits
14.    END IF
15. END FOR

16. RETURN hits
```

Time Complexity:
- Best Case: O(n)
- Worst Case: O(nm)

Space Complexity: O(k), where k is the number of matches.

## 5. Closest Login Locations – Brute Force

### Aim
Find the two login locations with the minimum Euclidean distance.

### Pseudocode

```text
CLOSEST_LOGINS(events)

1. IF number of events < 2
2.     RETURN NO PAIR
3. END IF

4. min_distance = INFINITY
5. pair = NONE

6. FOR i = 0 TO n - 1
7.     FOR j = i + 1 TO n - 1
8.         Calculate squared distance
9.         IF distance < min_distance
10.            min_distance = distance
11.            pair = (events[i], events[j])
12.        END IF
13.    END FOR
14. END FOR

15. RETURN pair and square root of min_distance
```

Time Complexity: O(n²)

Space Complexity: O(1)

## 6. Optimised Closest Pair with X-coordinate Pruning

### Aim
Reduce unnecessary distance calculations by sorting points according to their x-coordinate and pruning pairs that cannot improve the current minimum distance.

### Pseudocode

```text
OPTIMISED_CLOSEST_LOGINS(events)

1. IF number of events < 2
2.     RETURN NO PAIR
3. END IF

4. SORT events by x-coordinate
5. min_distance_squared = INFINITY
6. pair = NONE

7. FOR i = 0 TO n - 1
8.     FOR j = i + 1 TO n - 1
9.         dx = events[j].x - events[i].x

10.        IF dx * dx >= min_distance_squared
11.            BREAK
12.        END IF

13.        dy = events[j].y - events[i].y
14.        distance_squared = dx * dx + dy * dy

15.        IF distance_squared < min_distance_squared
16.            min_distance_squared = distance_squared
17.            pair = (events[i], events[j])
18.        END IF
19.    END FOR
20. END FOR

21. RETURN pair and square root of min_distance_squared
```

Time Complexity:
- Best/practical cases: Can be less than O(n²), depending on data.
- Worst Case: O(n²)

Space Complexity: O(n) for the sorted list.

## 7. Overall Complexity Comparison

| Algorithm | Original / Corrected | Optimised |
|---|---|---|
| Alert Sorting | O(n²) | O(n log n) worst case |
| IP Blocklist | O(n) | O(1) average lookup |
| Signature Matching | O(nm) | O(nm) worst case |
| Closest Pair | O(n²) | O(n²) worst case, with pruning |

