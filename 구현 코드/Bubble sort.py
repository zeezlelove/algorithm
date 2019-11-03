a = [1,10,5,8,7,6,4,3,2,9]
for i in range(10):
    for j in range(9-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
