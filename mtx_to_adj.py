def adjacency_list_to_adjacency_matrix(adj_list):
    num_vertices = len(adj_list)
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for u, edges in enumerate(adj_list):
        for v, w in edges:
            adj_matrix[u][v] = w

    return adj_matrix

# Given adjacency list
adj_list = [
    [(1, 5), (2, 10)],
    [(0, 5), (2, 3), (3, 20)],
    [(0, 10), (1, 3), (3, 2)],
    [(1, 20), (2, 2)]
]

adj_matrix = adjacency_list_to_adjacency_matrix(adj_list)
for row in adj_matrix:
    print(row)
