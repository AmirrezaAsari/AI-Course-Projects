# Benchmark Results for BFS, DFS and Bidirectional Search

I used the "benchmark" function to calculate the memory used and execution time for BFS, DFS, and bidirectional search algorithms. 
The graph provided is directed, so I did the benchmark for both directed and non-directed format when using bidirectional search.


## Directed
Benchmark results for searches when the graph is directed (is_directed field is True):

    Algorithm: bidirectional_search
    Execution time: 0.000205 seconds
    Memory used: 1.34 KB (peak: 4.36 KB)
    -------------------------------------------------------------------
    Algorithm: bfs_search
    Execution time: 0.000085 seconds
    Memory used: 0.12 KB (peak: 1.38 KB)
    -------------------------------------------------------------------
    Algorithm: dfs_search
    Execution time: 0.000070 seconds
    Memory used: 0.12 KB (peak: 0.70 KB)
    -------------------------------------------------------------------
as we see, when the graph is directed, the Bidirectional searches has more execution time that other algorithms. this is because when the graph is directed, when searching backward, we need to reverse the graph and search with that which causes it to take more time comparet to others. it also takes more memory.

   
## UnDirected
I also ran another benchmark where I considered the graph undirected (is_directed field is False). 

    Algorithm: bidirectional_search
    Execution time: 0.000079 seconds
    Memory used: 0.15 KB (peak: 2.15 KB)
    -------------------------------------------------------------------
    Algorithm: bfs_search
    Execution time: 0.000270 seconds
    Memory used: 0.12 KB (peak: 1.38 KB)
    -------------------------------------------------------------------
    Algorithm: dfs_search
    Execution time: 0.000126 seconds
    Memory used: 0.12 KB (peak: 0.70 KB)
    -------------------------------------------------------------------

When the graph is considered undirected, the bidirectional search algorithm is faster than the other two, which aligns with theoretical expectations.  
However, it requires more memory due to maintaining two frontiers.  
In this case, the memory usage is lower compared to directed version because there's no need to reverse the graph. But it's still more than two other algorithms, which is not what we expect theoretically. Well I think it can be because of the implementation, the graph we have and the start and goal node that we are running benchmark on and etc.
For a more realistic benchmark, we could test all nodes as both start and goal across multiple graphs and compute the average results. However, there's no need for that since we have theoretical expectations.

## Conclusion
The Bidirectional search is faster than the BFS and DFS search. Time complexity for BFS and DFS is: $$ O(b^m) $$
and for the Bidirectional search, we are actually running two searches at the same time, so the time complexity would be: $$ O\left(b^{\frac{m}{2}}\right)$$
Comparing memory usages, for BFS  its $$ O(b^m)$$ all nodes at the current level in the queue. But in DFS we store the nodes along the current path, so the complexity is $$O(bd)$$
for the Bidirectional search, we have two frontiers but we have half of it compared to BFS, so memory complexity is $$O\left(2b^{\frac{m}{2}}\right)$$
Overall, the bidirectional searches seems the best option since it has less time and space complexity.