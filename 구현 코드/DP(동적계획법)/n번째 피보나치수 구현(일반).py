def fibo(n):
    if 0 <= n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)
n = int(input())
print(fibo(n))
