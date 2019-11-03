def fibo(n):
    if n == 0:
        dp[n] = 0
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]
    else:
        if dp[n] > 0:
            return dp[n]
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
            return dp[n]
n = int(input())
dp = [0 for i in range(n+1)]
fibo(n)
print(dp)
