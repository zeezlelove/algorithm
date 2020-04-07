import sys
ip = sys.stdin.readline
class Node: #클래스를 이용해서 a정점에서 b정점까지 가중치 w로 만들었다.
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w

V,E = map(int,ip().split())
inf = 1000000000
arr = [0 for i in range(E+1)]
d = [inf for i in range(V+1)]
for i in range(1,E+1):
    a,b,c = map(int,ip().split())
    arr[i] = Node(a,b,c)

d[1] = 0
chk = False
# a정점에서 b정점으로 갈 때, 거리가 짧아지는 경우가 생긴다면 계속 업데이트를 해주는 방식이다.
# V(정점)*E(간선)번 반복후 종료 된다.
for i in range(1,V):
    for j in range(1,E+1):
        u,v,w = arr[j].u,arr[j].v,arr[j].w
        if d[u] != inf:
            d[v] = min(d[v],d[u]+w)

#음수사이클 체크
for i in range(1,E+1):
    u,v,w = arr[i].u,arr[i].v,arr[i].w
    if d[u] != inf and d[v] > d[u]+w: #또 갱신하는 경우가 생긴다면 음수사이클이므로 -1을 출력한다.
        chk = True
        break
if chk:
    print(-1)
else:
    for i in range(2,V+1):
        print(d[i] if d[i] != inf else -1)
#icpc.me/11657
