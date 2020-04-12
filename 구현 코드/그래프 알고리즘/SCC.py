from sys import *
setrecursionlimit(500000)
ip = stdin.readline
V,E = map(int,ip().split())
arr = [[] for i in range(V+1)]
d = [0 for i in range(V+1)] # 방문 순서
f = [False for i in range(V+1)] #scc가 확정된 정점 판별
scc = []
st = []
SccTotal,cnt = 0,0  #scc개수
for i in range(E):
    a,b = map(int,ip().split())
    arr[a].append(b)
def dfs(nd):
    global cnt,SccTotal
    cnt += 1
    d[nd] = cnt
    st.append(nd)

    p = d[nd]
    for i in arr[nd]:
        if d[i] == 0: #방문 안했을경우
            p = min(p,dfs(i))
        elif not f[i]: #방문을 했지만 scc가 확정이 안된경우
            p = min(p,d[i])
    if p == d[nd]: #현재노드의 cnt값과 현재 가장작은 cnt값이 같은경우(scc를 다돈경우)
        sc = []
        while 1:
            t = st.pop()
            sc.append(t)
            f[t] = True
            if t == nd:break
        sc.sort()
        scc.append(sc)
        SccTotal += 1

    return p
for i in range(1,V+1):
    if d[i] == 0:
        dfs(i)
scc.sort()
print(SccTotal)
for i in scc:
    print(*i,end=' ')
    print(-1)
