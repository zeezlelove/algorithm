inDegree = [0 for i in range(10)]
a = [[] for i in range(10)]
def topologySort():
    ret = [0 for i in range(10)]
    q = []
    #진입차수가 0인 노드를 큐에 삽입합니다.
    for i in range(1,n+1):
        if inDegree[i] == 0:q.append(i)
    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문합니다.
    while q:
        p = q.pop(0)
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
