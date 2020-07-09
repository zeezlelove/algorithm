def dfs(cnt):
    if len(Print) == M:
        for i in Print:
            print(i,end=' ')
        print()
    else:
        for i in range(N):
            if len(Print) < M:
                if not v.get(arr[i]):
                    Print.append(arr[i])
                    v[arr[i]] = 1
                    dfs(i+1)
                    v[arr[i]] = 0
                    Print.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
v = {}
Print = []
dfs(0)
