from collections import deque

def bfs_search(graph, start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        print('bfs: ', current)
        if current == goal:
            return return_path(visited, goal)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
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
    print("BFS Order:", bfs_search(graph, start, goal))