def snail(n):
    a = [[0 for i in range(n)] for i in range(n)]
    i,j,num = 0,-1,1
    chk = 1
    while n > 0:
        for _ in range(n): 
            j += chk
            a[i][j] = num
            num += 1
        n -= 1
        if n == 0:break
        for _ in range(n):
            i += chk
            a[i][j] = num
            num += 1
        chk *= -1
    return a
