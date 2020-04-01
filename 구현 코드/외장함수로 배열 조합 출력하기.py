from itertools import combinations
n = int(input()) #n개의 조합
arr = list(map(int,input().split()))
li = combinations(arr,n)
for i in li:
    print(i)
