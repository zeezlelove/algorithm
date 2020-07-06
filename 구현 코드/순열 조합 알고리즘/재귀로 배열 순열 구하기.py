def dfs():
    if len(Print) == m: #cnt가 k되었으므로 종료하고 출력한다.
        for i in Print:
            print(i,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if not v[i]:
                v[i] = 1
                Print.append(i)
                dfs()
                Print.pop()
                v[i] = 0
n,m = map(int,input().split())
v = [0 for i in range(n+1)]
Print = []
dfs()
#백준 N과 M
