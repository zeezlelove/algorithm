arr = [0,2,4,6,8,10,12,14,16,18,20]
s,e = 0,n-1
find_value = int(input())
while s <= e:
    mid = (s+e)//2
    if arr[mid] == find_value: #arr[mid]랑 찾는값이랑 같으면 "같습니다"출력
        print("값이 리스트안에 있습니다.")
        exit()
    if arr[mid] < find_value: #arr[mid]가 더작으면 앞에 값을 본다.
        s = mid+1
    if find_value < arr[mid]: #arr[mid]가 더크면 뒤에값을 본다.
        e = mid-1
print("값이 리스트 안에 없습니다.") #없으면 "없습니다"를 출력한다.
