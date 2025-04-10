def ids_search(graph, start, goal):
    depth = 0
    while True:
        print(depth)
        result = depth_limited_dfs(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1

def depth_limited_dfs(graph, start, goal, depth_limit):
    stack = [(start, 0)]  # (node, current_depth)
    visited = {start: None}
    path = []
    while stack:
        current, depth = stack.pop()
        path.append(current)
        print(f"current: {current}, depth: {depth}, path: {path}")
        print('----------------------------------------------------------------------------------')

        if current == goal:
            print('ids: ', path)
            return return_path(visited, goal)

        if depth < depth_limit:
              for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited[neighbor] = current
                    stack.append((neighbor, depth + 1))

    return None

def return_path(visited, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current]
    path.reverse()  # correct order
    return path


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': ['P', 'Q'],
        'I': ['R', 'S'],
        'J': ['T', 'U'],
        'K': ['V', 'W'],
        'L': ['X', 'Y'],
        'M': ['Z'],
    }

    start_node = 'A'
    goal_node = 'W'
    path = ids_search(graph, start_node, goal_node)
    if path:
        print("Path found:", path)
    else:
        print("No path exists between", start_node, "and", goal_node)
