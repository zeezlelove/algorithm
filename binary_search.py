def binary_search_recursion(target,low,high,data):
    data.sort()
    if low > high: #만약에 시작지점이 끝지점보다 크면
        return False ##True return
    mid = (low+high)//2 #mid 값을 지정해준다.
    if data[mid] == target: #만약에 mid값이랑 찾는값이랑 같으면
        return True #True return
    elif data[mid] > target: #만약에 mid값이 찾는값보다 크면
        high = mid - 1 #끝지점을 mid에서 1줄여준다.
    else: #만약에 mid값이 찾는값보다 작으면
        low = mid + 1 #시작지점을 mid에서 1을더해준다.
    return binary_search_recursion(target,low,high,data)
