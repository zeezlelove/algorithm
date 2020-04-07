array = [5,4,1,8,7,6,2,9,3]
for i in range(len(array)-1):
    j = i
    while j > 0 and array[j] > array[j+1]:
        array[j],array[j+1] = array[j+1],array[j]
        j -= 1
print(array)
