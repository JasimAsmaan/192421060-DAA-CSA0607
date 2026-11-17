"""Cross-check Dijkstra, Bellman-Ford and Floyd on random non-negative graphs."""
import random
from shortest_paths import dijkstra, bellman_ford, floyd_warshall, INF

random.seed(3)
for t in range(300):
    n = random.randint(2, 7)
    V = [chr(65 + i) for i in range(n)]
    E = [(u, v, random.randint(0, 9)) for u in V for v in V if u != v and random.random() < 0.4]
    D = floyd_warshall(V, E)
    for s in V:
        d1 = dijkstra(V, E, s)[0]
        d2, _, neg = bellman_ford(V, E, s)
        assert not neg and d1 == d2
        for j, v in enumerate(V):
            assert d1[v] == D[V.index(s)][j], (E, s, v)
print("PASS: Dijkstra == Bellman-Ford == Floyd on 300 random graphs")
