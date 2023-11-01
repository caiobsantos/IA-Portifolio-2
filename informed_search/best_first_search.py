graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}

initial = 0
goal = 4

def heuristic(node, goal):
    return abs(node - goal)

# Define the Best-First Search algorithm
def bfs(graph, initial, goal):
    open_list = [(heuristic(initial, goal), initial)]
    came_from = {}

    came_from[initial] = None

    while open_list:
        open_list.sort()
        _, current = open_list.pop(0)

        if current == goal:

            result = []
            while current is not None:
                result.append(current)
                current = came_from[current]
            result.reverse()
            return result

        for neighbor in graph[current]:
            if neighbor not in came_from:
                open_list.append((heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current

    return None  # result not found

result = bfs(graph, initial, goal)

if result:
    print("Caminho encontrado: ", result)
else:
    print("Caminho não encontrado")
