"""Task 5 - Dijkstra, Bellman-Ford and Floyd-Warshall on the given graph."""
import heapq

INF = float("inf")
VERTICES = ["A", "B", "C", "D", "E"]
EDGES = [("A", "B", 4), ("A", "C", 7), ("B", "C", 2), ("B", "D", 6),
         ("C", "D", 1), ("D", "E", 3), ("C", "E", 8)]


def dijkstra(vertices, edges, source):
    adj = {v: [] for v in vertices}
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = {v: INF for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0
    pq = [(0, source)]
    done = set()
    order = []
    while pq:
        d, u = heapq.heappop(pq)           # selection: smallest tentative distance
        if u in done:
            continue
        done.add(u)
        order.append((u, d))
        for v, w in adj[u]:                # relaxation
            if v in done:                  # greedy commitment: finalised vertices never change
                continue
            if d + w < dist[v]:
                dist[v] = d + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, pred, order


def bellman_ford(vertices, edges, source):
    dist = {v: INF for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                changed = True
        if not changed:
            break
    neg_cycle = any(dist[u] != INF and dist[u] + w < dist[v] for u, v, w in edges)
    return dist, pred, neg_cycle


def floyd_warshall(vertices, edges):
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
    for u, v, w in edges:
        D[idx[u]][idx[v]] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D


def path(pred, target):
    p = []
    while target is not None:
        p.append(target)
        target = pred[target]
    return "->".join(reversed(p))


if __name__ == "__main__":
    print("=== 5.1 Dijkstra from A ===")
    dist, pred, order = dijkstra(VERTICES, EDGES, "A")
    print("Extraction order:", order)
    for v in VERTICES:
        print(f"  dist[{v}] = {dist[v]}, path = {path(pred, v)}")

    print("\n=== 5.2 Bellman-Ford from A (non-negative graph) ===")
    d2, p2, neg = bellman_ford(VERTICES, EDGES, "A")
    print("dist =", d2, " negative cycle:", neg)

    print("\nBellman-Ford with a negative edge (D->C = -5 added -> creates cycle C->D->C of weight -4)")
    d3, p3, neg3 = bellman_ford(VERTICES, EDGES + [("D", "C", -5)], "A")
    print("negative cycle reachable:", neg3)

    print("\nBellman-Ford with negative edge but no cycle (B->C = -3 instead of 2)")
    edges_neg = [("A", "B", 4), ("A", "C", 7), ("B", "C", -3), ("B", "D", 6),
                 ("C", "D", 1), ("D", "E", 3), ("C", "E", 8)]
    d4, p4, neg4 = bellman_ford(VERTICES, edges_neg, "A")
    print("dist =", d4, " negative cycle:", neg4)

    print("\nWhy greedy commitment fails: small graph A->B=2, A->C=3, C->B=-2")
    V2 = ["A", "B", "C"]
    E2 = [("A", "B", 2), ("A", "C", 3), ("C", "B", -2)]
    dd, _, order2 = dijkstra(V2, E2, "A")
    print("Dijkstra  : dist[B] =", dd["B"], "(B was finalised at 2 before C was processed)")
    db, _, negb = bellman_ford(V2, E2, "A")
    print("BellmanFord: dist[B] =", db["B"], "(true shortest path A->C->B = 1)")

    print("\n=== 5.3 Floyd-Warshall all-pairs ===")
    D = floyd_warshall(VERTICES, EDGES)
    print("     " + " ".join(f"{v:>4}" for v in VERTICES))
    for i, v in enumerate(VERTICES):
        print(f"{v:>4} " + " ".join(f"{('INF' if x == INF else x):>4}" for x in D[i]))
