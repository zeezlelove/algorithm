def func(cnt):
    if cnt == k: #cnt가 k되었으므로 종료하고 출력한다.
        for i in v:
            print(i,end=' ')
        print()
    else:
        for i in range(len(arr)):
            if li[i]:continue
            li[i] = 1
            v.append(arr[i])
            func(cnt+1)
            v.pop()
            li[i] = 0
k = int(input())
li = [0 for i in range(k)]
v = []
arr = list(map(int,input().split()))
func(0)
