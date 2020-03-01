def maxFlow(s,e):
    global ret
    while 1:
        d = [-1 for i in range(n+1)]
        q = []
        q.append(s)
        while q:
            x = q.pop(0)
            for y in arr[x]:
                # 방문하지 않은 노드 중에 용량이 남은 경우
                if c[x][y] - f[x][y] > 0 and d[y] == -1:
                    q.append(y)
                    d[y] = x # 경로를 기억합니다.
                    if y == e:break # 도착지에 도달한경우
        if d[e] == -1:break # 모든경우를 찾은뒤에 탈출한다.
        fl = inf
        i = e
        while i != s: # 거꾸로 최소 유량 탐색
            fl = min(fl,c[d[i]][i]-f[d[i]][i])
            i = d[i]
        i = e
        while i != s:
            f[d[i]][i] += fl
            f[i][d[i]] -= fl
            i = d[i]
        ret += fl
n = int(input())
inf,ret  = 1e9,0
c = [[0 for i in range(n+1)] for i in range(n+1)] # u에서 v로 가는 간선용량
f = [[0 for i in range(n+1)] for i in range(n+1)] # u에서 v로 실제로 흐르는 유량
arr = [[] for i in range(n+1)] #연결되어있는 노드들
for i in range(10):
    a,b,co = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    c[a][b] = co
maxFlow(1,n)
print(ret)
