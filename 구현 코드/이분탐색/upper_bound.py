n = int(input())
arr = sorted(list(map(int,input().split())))
def upper_bound(val):
    s,e,ans = 0,n-1,1e9
    while s <= e:
        mid = (s+e)//2
        if arr[mid] <= val:
            s = mid+1
        else:
            if ans > mid:
                ans = mid
            e = mid-1
    return ans
print(upper_bound(int(input())))
