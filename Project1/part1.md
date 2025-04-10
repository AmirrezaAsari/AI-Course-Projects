# Bidirectional Search
Bidirectional search is one of the graph search algorithms. The main idea is that we start from both start and end(goal) side, and search from them. We do one BFS/DFS from start node and another from goal node, by doing this, somewhere at the middle we reach to the same node from both sides, and thats the shortest path that we are looking for, this makes the algorithm to work faster compared to BFS and DFS. It also requires less memory space. the memory and time complexity are disgussed more [here](https://github.com/AmirrezaAsari/AI-projects/blob/master/Project1/benchmark_results.md).

for example, for this simple graph: 
![Tree (graph theory) - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Tree_graph.svg/1200px-Tree_graph.svg.png)
consider we want to find  the shortes path from 1 to 6, the algorithm works like this.
first, we start from 1, at the same time we also start from 6, so we expand the 1 and the frontier list would be [4], we also do this for the 6 and we get the frontier list [5]. 
then we start from forward 4 and we expand it and the frontier list result will be [2, 3], we do the same to 5 and get [4]. so we see that we reached 4, wich was in the forward_visited list, so we see that we have a path from 1 to 4, and we also see that we have a path from 6 to 4, which we can conclude that there's a path from 1 to 6. and we combine the two visited lists and we get the shortest path from 1 to 6.

So, we were able to find the path without needing to going from 1 to 2, 1 to 3, 1 to 5, and then 1 to 6, we do two searches at the same time and get better time and memory complexity.

##  Implementation
In order to implement this algorithm, we need a function and the graph, start node, goal node and is_directed as the inputs.

In bidirectional search, we need to know if the graph is directed or not. When the graph is directed, its ok when forward searching, but backward would be a problem, we are defining a graph as a dictionary containing a node and a list of its children, so when doing backward search, we need to reverse the graph so when starting from goal node, so we have also have a function to reverse the graph.

after the algorithm finds the node that is in share, it should return the path, so we have another function to create the path based on the forward_visited and backward_visited lists and the meeting_point node.

#### bidirectional search function 
To implement the actual function, we need a queue for forward and backward, we need these queues to know that what nodes are we going to expand.
We need to store visited nodes for both forward and backward so we can have the path and check that if they meet or not. we are using a dictionary (hash table) for this because we also want to know the path.

Both from forward and backward the function pops from the queue and get the neighbors of that node, and for each neighbor if its not visited, it adds it to visited and queue so we know that we visited this node and are going to expand it. in each forward and backward if the neighbor node that we are expanding is in the other visited list, its the path that we are looking to, so we use the return_path function to use visited lists and meeting point to create the result.
If we dont get to ant meeting points, it means that there's no answer.
also theres a condition in backward searching that checks if the graph is directed to use reversed graph or not.