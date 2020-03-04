def func(ix1,ix2):
    if ix2 == 6:
        for i in lotto:
            print(i,end=' ')
        print()
    else:
        for i in range(ix1,k):
            lotto[ix2] = arr[i]
            func(i+1,ix2+1)
while 1:
    lotto = [0 for i in range(6)]
    arr = list(map(int,input().split()))
    k = arr.pop(0)
    if k == 0:break
    func(0,0)
    print()
