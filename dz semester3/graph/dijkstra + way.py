import math


def Dijkstra(S, F, matrix):
    N = len(graph)
    valid = [True] * N
    weight = [math.inf] * N
    weight[S] = 0
    way = []
    for i in range(N):
        min_weight = math.inf
        ID_min_weight = -1
        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j
                way.append([j])
        for z in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]

        valid[ID_min_weight] = False
        if ID_min_weight == F:
            break
    return weight[F], way


graph = [[math.inf, 3, math.inf, 1, 15],
         [3, math.inf, 7, 11, 5],
         [math.inf, 7, math.inf, 5, 8],
         [1, 11, 5, math.inf, 11],
         [15, 5, 8, 11, math.inf]]

Start = 0
Finish = 4

print(Dijkstra(Start, Finish, graph))
