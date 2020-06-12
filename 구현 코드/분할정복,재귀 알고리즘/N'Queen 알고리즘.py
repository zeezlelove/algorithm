def checking(x):
    for i in range(x):
        if r[x] == r[i] or abs(r[x] - r[i]) == x - i:
            return False
    return True


def dfs(x):
    global ret

    if x == N:
        ret += 1
    else:
        for i in range(N):
            r[x] = i
            if checking(x):
                dfs(x+1)
N = int(input())
r = [0] * N
ret = 0
dfs(0)
print(ret)
# 12이상은 매우 오래 걸림
