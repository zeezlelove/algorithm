from sys import *
ip = stdin.readline
n = int(ip())
arr = sorted(list(map(int,ip().split())))
tar = int(ip())
def lower_bound(val):
    s,e,ans = 0,n-1,1e9
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < val:
            s = mid+1
        else:
            e = mid-1
    return e
def upper_bound(val):
    s,e,ans = 0,n-1,1e9
    while s <= e:
        mid = (s+e)//2
        if arr[mid] <= val:
            s = mid+1
        else:
            e = mid-1
    return e
print(upper_bound(tar)-lower_bound(tar),end=' ')
#
