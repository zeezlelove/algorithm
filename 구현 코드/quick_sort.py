arr = list(map(int,input().split())) # [10 9 8 7 6 5 4 3 2 1]
def quick_sort(l,r):
    if l >= r:return
    i,j = l,r
    pivot = arr[(l+r)//2]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    quick_sort(l,j)
    quick_sort(i,l)
quick_sort(0,len(arr)-1)
print(arr) #[1 2 3 4 5 6 7 8 9 10]
