from itertools import permutations
n = int(input()) #n개의 순열
arr = list(map(int,input().split()))
li = permutations(arr,n)
for i in li:
    print(i)
