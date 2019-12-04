inDegree = [0 for i in range(10)]
a = [[] for i in range(10)]
def topologySort():
    ret = [0 for i in range(10)]
    q = []
    #진입차수가 0인 노드를 큐에 삽입합니다.
    for i in range(1,n+1):
        if inDegree[i] == 0:q.append(i)
    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문합니다.
    for i in range(1,n+1):
        # n개를 방문하기 전에 큐가 비어버리면 사이클발생
        if len(q) == 0:
            print("사이클 발생")
            return
        p = q.pop(0)
        ret[i] = p
        for i in range(len(a[p])):
            y = a[p][i]
            # 새롭게 진입차수가 0이 된 정점을 큐에 삽입합니다.
            inDegree[y] -= 1
            if inDegree[y] == 0:
                q.append(y)
    for i in range(1,n+1):
        print(ret[i])
n = 7
a[1].append(2)
inDegree[2] += 1

a[1].append(5)
inDegree[5] += 1

a[2].append(3)
inDegree[3] += 1

a[3].append(4)
inDegree[4] += 1

a[4].append(6)
inDegree[6] += 1

a[5].append(6)
inDegree[6] += 1

a[6].append(7)
inDegree[7] += 1
topologySort()
