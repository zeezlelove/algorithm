a = [[] for i in range(10)]
v = [False for i in range(10)]
ans = []
def dfs(nd):
    if v[nd]:return
    v[nd] = True
    for i in a[nd]:
        if v[i] == False:
            dfs(i)
    ans.append(nd)

n = 7
a[1].append(2)

a[1].append(5)

a[2].append(3)

a[3].append(4)

a[4].append(6)

a[5].append(6)

a[6].append(7)
for i in range(1,n+1):
    if not v[i]:
        dfs(i)
print(ans)
