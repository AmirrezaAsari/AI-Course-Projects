def dfs_search(graph, start, goal):
    stack = [start]
    visited = {start: None}

    while stack:
        current = stack.pop()
        print('dfs: ', current)
        if current == goal:
            return return_path(visited, goal)
        for neighbor in reversed(graph.get(current, [])):  # reversed for standard DFS order
            if neighbor not in visited:
                visited[neighbor] = current
                stack.append(neighbor)
    return None


def return_path(visited, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current]
    path.reverse()
    return path



if __name__ == "__main__":
    graph = {
        'A': ['F', 'G', 'L'],
        'F': ['P', 'Q'],
        'P': ['G'],
        'G': ['Q', 'R'],
        'Q': ['H'],
        'H': ['R', 'S'],
        'R': ['I'],
        'I': ['S', 'T'],
        'S': ['J'],
        'J': ['T', 'B'],
        'B': ['H', 'I', 'M'],
        'T': ['K'],
        'M': ['C'],
        'C': ['J', 'N', 'K'],
        'N': ['D'],
        'K': ['D', 'A'],
        'D': ['O', 'M'],
        'L': ['B'],
        'O': ['E'],
        'E': ['O', 'N', 'P'],
    }


    start = 'A'
    goal = 'E'
    print("DFS search:", dfs_search(graph, start, goal))