import math

infinity = math.inf


graph = [
    [0, 1, 6, 6, 21],
    [infinity, 0, 5, 5, infinity],
    [infinity, infinity, 0, infinity, 12],
    [infinity, infinity, 4, 0, 4],
    [infinity, infinity, infinity, infinity, 0],
]

for i in range(len(graph)):
    for j in range(len(graph)):
        for k in range(len(graph)):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


for line in graph:
    print(line)

