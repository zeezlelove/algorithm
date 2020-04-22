def getParent(p,x):
    if p[x] == x:
        return x
    p[x] = getParent(p,p[x])
    return p[x]
def unionParent(p,a,b):
    a = getParent(p,a)
    b = getParent(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
def findParent(p,a,b):
    a = getParent(p,a)
    b = getParent(p,b)
    if a == b:
        return 1
    return 0
