def Sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans

def update(i,dif):
    while i < len(tree):
        tree[i] += dif
        i += (i & -i)

n,m,k = map(int,input().split())
tree = [0 for i in range(n+1)]
arr = [0 for i in range(n+1)]
for i in range(1,n+1):
    arr[i] = int(input())
    update(i,arr[i])

for i in range(m+k):
    t,a,b = map(int,input().split())
    if t == 1:
        dif = b-arr[a]
        arr[a] = b
        update(a,dif)
    else:
        print(Sum(b)-Sum(a-1))
