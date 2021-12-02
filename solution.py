from sys import stdin

# test case 수
T = int(stdin.readline().rstrip())

for t in range(1, T + 1):
    # 방석의 크기 N
    N = int(stdin.readline().rstrip())
    # 방석에 적혀진 단어들
    cushion = [stdin.readline().rstrip().split() for _ in range(N)]
    # 각 단어와 그 수에 대한 dictionary
    words = dict()
    for row in cushion:
        for elem in row:
            if elem not in words:
                words[elem] = 1
            else:
                words[elem] += 1
    # 가장 많이 있는 단어
    maxKey = max(words, key=words.get)
    maxVal = words[maxKey]
    # MST
    def make(edges):
        parents = dict()
        for edge in edges:
            parents[edge] = edge
        return parents

    def find(parents, edge):
        if parents[edge] != edge:
            parents[edge] = find(parents, parents[edge])
        return parents[edge]

    def union(parents, a, b):
        a = find(parents, a)
        b = find(parents, b)
        if a == b:
            return False
        parents[b] = a
        return True

    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    edges = []
    edgeDict = dict()
    for r in range(N):
        for c in range(N):
            if cushion[r][c] == maxKey:
                edges.append((r, c))
                for dr, dc in zip(dx, dy):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and cushion[nr][nc] == maxKey:
                        A, B = (r, c), (nr, nc)
                        if r > nr or (r == nr and c > nc):
                            A, B = B, A
                        if (A, B) not in edges:
                            edgeDict[(A, B)] = 0.5 * (abs(dr) + abs(dc)) + 0.5

    parents = make(edges)
    edgeList = list(zip(edgeDict.keys(), edgeDict.values()))
    edgeList.sort(key=lambda x: x[1])
    result = 0
    count = 0
    for edge in edgeList:
        if union(parents, edge[0][0], edge[0][1]):
            result += edge[1]
            count += 1
            if count == maxVal - 1:
                break
    # 결과 출력
    print("#" + str(t), end=" ")
    if count < maxVal - 1:
        print("고양이 승!")
    else:
        print(result)