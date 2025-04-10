from bfs_search import bfs_search
from dfs_search import dfs_search
from bidirectional_search import bidirectional_search
import time
import tracemalloc

def benchmark(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()

    result = func(*args, **kwargs)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Algorithm: {func.__name__}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Memory used: {current / 1024:.2f} KB (peak: {peak / 1024:.2f} KB)")
    print("-------------------------------------------------------------------")

    return result


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
goal = 'L'
is_directed = False

benchmark(bidirectional_search, graph, start, goal, is_directed)
benchmark(bfs_search, graph, start, goal)
benchmark(dfs_search, graph, start, goal)
