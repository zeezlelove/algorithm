n,m = map(int,input().split())
q = [i+1 for i in range(n)]
print("<",end="")
for i in range(n-1):
    for j in range(m-1):
        q.append(q.pop(0))
    print(q.pop(0),end=", ")
print(q.pop(0),end=">")
