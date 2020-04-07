import queue as Q
import sys
ip = sys.stdin.readline
v,e = map(int, ip().split())
s = int(ip())

adj = [[] for i in range (v+1)]
d = [10000000]*(v+1)
for i in range(e):
    a, b, c = map(int,ip().split())
    adj[a].append((b, c))

def dijkstra(s):
    q = Q.PriorityQueue()
    q.put((0, s))
    d[s] = 0
    while not q.empty():
        pp = q.get()
        here = pp[1]
        dist = pp[0]
        if d[here] < dist:
            continue
        for i in adj[here]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                q.put((cost, i[0]))
dijkstra(s)

for i in range (1,v+1):
    if d[i] == 10000000:
        print("INF")
    else:
        print(d[i])
