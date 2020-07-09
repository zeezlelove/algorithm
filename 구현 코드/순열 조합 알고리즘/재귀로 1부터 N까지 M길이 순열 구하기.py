def dfs():
    if len(Print) == M: #cnt가 k되었으므로 종료하고 출력한다.
        for i in Print:
            print(i,end=' ')
        print()
    else:
        for i in range(1,N+1):
            if not v[i]:
                v[i] = 1
                Print.append(i)
                dfs()
                Print.pop()
                v[i] = 0
N,M = map(int,input().split())
v = [0 for i in range(N+1)]
Print = []
dfs()
#백준 N과 M 1
