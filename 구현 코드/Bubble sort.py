n = int(input()) #배열의 크기
a = list(map(int,input().split()))
for i in range(n):
    for j in range((n-1)-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
