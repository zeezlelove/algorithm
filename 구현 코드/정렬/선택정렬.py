arr = [10,9,8,7,6,5,4,3,2,1]
for i in range(len(arr)):
    min = 9999
    for j in range(i,len(arr)):
        if min > arr[j]:
            min = arr[j]
            idx = j
    arr[i],arr[idx] = arr[idx],arr[i]
print(arr) # [1,2,3,4,5,6,7,8,9,10]
