n = int(input())
arr = list(map(int,input().split()))
def lower_bound(val):
    s,e,ans = 0,n-1,1e9
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < val:
            s = mid+1
        else:
            ans = min(ans,mid)
            e = mid-1
    return ans
print(lower_bound(int(input())))
