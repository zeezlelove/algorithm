def Sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i) #최하위 비트를 없애면서 구간합을 더해준다.
    return ans

def update(i,dif):
    while i < len(tree):
        tree[i] += dif # 차이를 더한다
        i += (i & -i) # Sum함수와 다르게 최하위 비트를 더해서 업데이트해준다.

n,m,k = map(int,input().split())
tree = [0 for i in range(n+1)] # 홀수인덱스는 입력받은 배열의 값과 같다.
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
        # 구간합 sum(arr[i]~arr[j])는 sum(arr[1]~arr[j])에서 arr[1]~arr[i-1]을 뺀 값과 같다
        print(Sum(b)-Sum(a-1))
