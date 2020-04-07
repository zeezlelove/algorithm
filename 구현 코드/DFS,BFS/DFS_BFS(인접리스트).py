import sys
sys.setrecursionlimit(50000)
n,m,s = map(int,input().split())
arr = [[] for i in range(n+1)]
v = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(len(arr)):
    arr[i] = sorted(arr[i])
def dfs(nd,n):
    v[nd] = True
    print(nd,end=' ')
    for i in range(len(arr[nd])):
        if v[arr[nd][i]] == False:
            dfs(arr[nd][i],n)
dfs(s,n)
print()
v = [False for i in range(n+1)]
q = [s]
v[s] = True
while q:
    p = q.pop(0)
    print(p,end=' ')
    for i in range(len(arr[p])):
        if v[arr[p][i]] == False:
            q.append(arr[p][i])
            v[arr[p][i]] = True
#백준 1260번
