def func(ix,cnt):
    if cnt == k: #cnt가 k되었으므로 종료하고 출력한다.
        for i in li:
            print(i,end=' ')
        print()
    else:
        for i in range(ix,len(arr)): #자신의 현재값보다 작은값은보지 않는다.
            li[cnt] = arr[i]
            func(i+1,cnt+1)
k = int(input())
li = [0 for i in range(k)]
arr = list(map(int,input().split()))
func(0,0)
print()
