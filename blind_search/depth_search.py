graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L'],
    'G': ['M', 'N'],
    'H': ['O'],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}

initial_node = 'A'
goal = 'I'

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path:
                return new_path

    return None

result = dfs(graph, initial_node, goal)
if result:
    print('Caminho de {} para {}: {}'.format(initial_node, goal, ' -> '.join(result)))
else:
    print(f'Nenhum caminho encontrado de {initial_node} para {goal}')
