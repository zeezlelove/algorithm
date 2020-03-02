def maxFlow(s,e):
    global ret
    while 1: #반복적으로 모든경우를 탐색할수있돋록 해준다.
        d = [-1 for i in range(n+1)] #방문 체크
        q = []
        q.append(s) # 시작점을 넣어준다.
        #일반적인 bfs를 실행한다, 인접한노드를 전부 본다.
        while q:
            x = q.pop(0)
            for y in arr[x]:
                # 방문하지 않은 노드 중에 용량이 남은 경우
                if c[x][y] - f[x][y] > 0 and d[y] == -1:
                    q.append(y)
                    d[y] = x # 경로를 기억합니다.
                    if y == e:break # 도착지에 도달한경우
        if d[e] == -1:break # 모든경우를 찾은뒤에 탈출한다.
        fl = inf # 가능한경로에서 최솟값을 찾아줘야하기 때문에 jnf로 둔다.
        i = e
        while i != s: # 거꾸로 최소 유량 탐색
            fl = min(fl,c[d[i]][i]-f[d[i]][i]) # 해당간선의 남은유량만큼 확인해서 가장최솟값을 넣어준다.
            i = d[i]
        i = e
        # 남아있는 더많은 경우를 찾기위해서 음의 유량도 봐준다.
        while i != s:
            f[d[i]][i] += fl #양의 유량
            f[i][d[i]] -= fl #음의 유량
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
