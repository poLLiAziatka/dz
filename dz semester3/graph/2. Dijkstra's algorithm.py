import math

graph = [[math.inf, 3, math.inf, 1, 15],
         [3, math.inf, 7, 11, 5],
         [math.inf, 7, math.inf, 5, 8],
         [1, 11, 5, math.inf, 11],
         [15, 5, 8, 11, math.inf]]

N = len(graph)
visit = [True] * N
min_graph = [math.inf] * N
min_graph[0] = 0
way = [[0, 0, 0]]

for i in range(N):
    min_weight = math.inf
    ID_min_weight = -1

    for j in range(N):
        if visit[j] and min_graph[j] < min_weight:
            min_weight = min_graph[j]
            ID_min_weight = j

    for z in range(N):
        if min_graph[ID_min_weight] + graph[ID_min_weight][z] < min_graph[z]:
            min_graph[z] = min_graph[ID_min_weight] + graph[ID_min_weight][z]
            print(ID_min_weight, z, min_graph[z])
    visit[ID_min_weight] = False

print(min_graph)
