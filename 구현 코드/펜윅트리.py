def sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i) #최하위 비트를 없애면서 구간합을 더해준다.
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
    update(i,arr[i]) #펜윅트리를 업데이트한다.

for i in range(m+k):
    t,a,b = map(int,input().split())
    if t == 1:
        dif = b-arr[a]
        arr[a] = b
        update(a,dif)
    else:
        print(sum(b)-sum(a-1))
