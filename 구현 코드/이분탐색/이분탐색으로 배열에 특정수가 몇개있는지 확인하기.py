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
# lower_bound는 tar값의 이상값의 인덱스 upper_bound는 초과값의 인덱스이므로 둘이 upper_bound에서 lower_bound를 빼주면 된다.
