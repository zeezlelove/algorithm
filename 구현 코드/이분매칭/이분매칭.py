n = int(input())
m = int(input())
arr = [[] for i in range(n+1)]
d = [0 for i in range(n+1)] #선택하는 노드
c = [False for i in range(n+1)]

#매칭성공 True, 실패한경우 False
def dfs(nd):
    # 연결된 모든노드에 대해서 들어갈수있는지 시도
    for i in arr[nd]:
        # 이미 처리한 노드는 볼 필요가 없음
        if c[i]:continue
        c[i] = True
        # 비어있거나 점유 노드에 더 들어갈 공간이 있는지 체크
        if d[i] == 0 or dfs(d[i]):
            d[i] = nd
            return True
    return False

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
cnt = 0
for i in range(1,n+1):
    c = [False for i in range(n+1)]
    if dfs(i):cnt += 1
print("매칭성공:",i)
for i in range(1,n+1):
    if d[i] != 0:
        print(d[i],i)
