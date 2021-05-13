import math

graph = [[math.inf, 5, math.inf, 11, 7, math.inf, math.inf],
         [5, math.inf, 7, 11, 2, 3, math.inf],
         [math.inf, 7, math.inf, math.inf, math.inf, 1, math.inf],
         [11, 11, math.inf, math.inf, 2, math.inf, 10],
         [7, 2, math.inf, 2, math.inf, 7, math.inf],
         [math.inf, 3, 1, math.inf, 7, math.inf, 7],
         [math.inf, math.inf, math.inf, 10, math.inf, 7, math.inf]]

min_graph = [0] * (len(graph))

# минимальные ребра
for i in range(len(graph)):
    min_graph[i] = [min(graph[i]), i, graph[i].index(min(graph[i]))]

# сортировка ребер
for i in range(len(min_graph) - 1):
    for j in range(len(min_graph) - 1):
        if min_graph[j][0] > min_graph[j + 1][0]:
            min_graph[j], min_graph[j + 1] = min_graph[j + 1], min_graph[j]

# строим минимальное остовное дерево, исключая циклы
temp = []
for i in range(len(min_graph)):
    if not (min_graph[i][1] in temp and min_graph[i][2] in temp):
        print(f"{min_graph[i][1]} -  {min_graph[i][2]} : {min_graph[i][0]}")
        temp.append(min_graph[i][1])
        temp.append(min_graph[i][2])
