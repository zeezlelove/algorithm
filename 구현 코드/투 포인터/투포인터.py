n,m = map(int,input().split()) #n: array 길이,m: 구할합
arr = list(map(int,input().split()))
end = 0
Sum = 0
ans = 0
for start in range(n):
    while end < n and Sum < m:
        Sum += arr[end]
        end += 1
    if Sum == m:
        ans += 1
    Sum -= arr[start]
print(ans) #m의 합이 되는 경우의수
