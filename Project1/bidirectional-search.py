from collections import deque, defaultdict

def bidirectional_search(graph, start, goal, is_directed):
    if start == goal:
        return [start]
    
    if (is_directed == True): # when graph is directed, we need the reverse in backward search
        reverse_graph = build_reverse_graph(graph);
    
    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visited = {start: None}
    backward_visited = {goal: None}

    while forward_queue and backward_queue:
        if forward_queue:
            current_forward = forward_queue.popleft()
            for neighbor in graph.get(current_forward, []):
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current_forward
                    forward_queue.append(neighbor)
                    if neighbor in backward_visited:
                        return return_path(forward_visited, backward_visited, neighbor)

        if backward_queue:
            current_backward = backward_queue.popleft()
            if (is_directed == True):
                for neighbor in reverse_graph.get(current_backward, []):
                    if neighbor not in backward_visited:
                        backward_visited[neighbor] = current_backward
                        backward_queue.append(neighbor)
                        if neighbor in forward_visited:
                            return return_path(forward_visited, backward_visited, neighbor)
                        
            if (is_directed == False): 
                for neighbor in graph.get(current_backward, []):
                    if neighbor not in backward_visited:
                        backward_visited[neighbor] = current_backward
                        backward_queue.append(neighbor)
                        if neighbor in forward_visited:
                            return return_path(forward_visited, backward_visited, neighbor)

    return None

def return_path(forward_visited, backward_visited, meeting_point):
    # start to meeting point
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = forward_visited[current]
    path.reverse()  # correct order

    # meeting point to goal
    current = backward_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = backward_visited[current]

    return path


def build_reverse_graph(graph): # we need this when the graph is directed.
    reverse_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reverse_graph[v].append(u)
    return reverse_graph



if __name__ == "__main__":
    graph = {
        'A': ['F', 'G', 'L'],
        'F': ['p', 'Q'],
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


    start_node = 'A'
    goal_node = 'E'
    is_directed = True

    path = bidirectional_search(graph, start_node, goal_node, is_directed)
    if path:
        print("Shortest path:", path)
    else:
        print("No path exists between", start_node, "and", goal_node)