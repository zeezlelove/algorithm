arr = list(map(int,input().split()))
def quick_sort(l,r):
    i,j = l,r
    pivot = arr[(l+r)//2]
    while arr[i] < pivot:
        i += 1
    while arr[j] > pivot:
        j -= 1
    if i <= j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    while i <= j:
        if l < j:
            quick_sort(l,j)
        if i < r:
            quick_sort(i,r)
