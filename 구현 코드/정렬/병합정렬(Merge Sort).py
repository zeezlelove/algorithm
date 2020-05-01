n = int(input())
arr = list(map(int,input().split()))
def merge(s,mid,e): #병합함수
    i,j,k = s,mid+1,s #i:분할된 왼쪽배열 인덱스,j:분할된 두번째 배열의 인덱스,k:ans의 인덱스
    ans = [0]*n
    while i <= mid and j <= e:
        if arr[i] <= arr[j]: #if 만약에 arr[i]가 더작으면 ans[k]에 arr[i]를 넣고 i에 1을 더한다.
            ans[k] = arr[i]
            i += 1
        else: #아니면 ans[k]에 arr[j]를 넣고 j에 1을 더한다.
            ans[k] = arr[j]
            j += 1
        k += 1
    while j <= e: #만약에 왼쪽 블럭이 남아있으면 남아있는 수를 ans에 넣는다.
        ans[k] = arr[j]
        k += 1
        j += 1
    while i <= mid: #만약에 오른쪽 블럭이 남아있으면 남아있는수를 ans에 넣는다.
        ans[k] = arr[i]
        k += 1
        i += 1
    for i in range(s,e+1):
        arr[i] = ans[i]
def mergeSort(s,e):
    # 분할 1개씩 될때 까지 계속한다.
    if s < e:
        mid = (s+e)//2
        mergeSort(s,mid) # 왼쪽 블럭 분할
        mergeSort(mid+1,e) # 오른쪽 블럭 분할
        merge(s,mid,e) # 분할블럭 병합
mergeSort(0,n-1)
for i in arr:
    print(i,end=' ')
