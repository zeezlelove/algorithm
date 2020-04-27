n = int(input())
arr = list(map(int,input().split()))
def lower_bound(val):
    s,e,ans = 0,n-1,1e9
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < val: #mid값이 찾으려는 값보다 작으면
            s = mid+1
        else: #mid값이 찾으려는 값보다 크면
            ans = min(ans,mid) #갱신
            e = mid-1
    return ans
print(lower_bound(int(input())))
