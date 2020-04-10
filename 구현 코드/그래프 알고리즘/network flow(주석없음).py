def maxFlow(s,e):
    global ret
    while 1: 
        d = [-1 for i in range(n+1)]
        q = []
        q.append(s)
        while q:
            x = q.pop(0)
            for y in arr[x]:
                if c[x][y] - f[x][y] > 0 and d[y] == -1:
                    q.append(y)
                    d[y] = x
                    if y == e:break
        if d[e] == -1:break
        fl = inf
        i = e
        while i != s:
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
c = [[0 for i in range(n+1)] for i in range(n+1)]
f = [[0 for i in range(n+1)] for i in range(n+1)]
arr = [[] for i in range(n+1)]
for i in range(10):
    a,b,co = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    c[a][b] = co
maxFlow(1,n)
print(ret)
