n,m,v = map(int,input().split())
arr = [[0 for i in range(n)] for i in range(n)]
visited = [False for i in range(n)]
q = []
for i in range(m):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
def dfs(s,n):
    visited[s] = True
    print(s+1,end=' ')
    for i in range(n):
        if arr[s][i] == 1 and visited[i] == False:
            dfs(i,n)
dfs(v-1,n)
print()
visited = [False for i in range(n)]
q.append(v-1)
visited[v-1] = True
while len(q) != 0:
    p = q.pop(0)
    print(p+1,end=' ')
    for i in range(n):
        if arr[p][i] == 1 and visited[i] != True:
            visited[i] = True
            q.append(i)
#백준 1260번
