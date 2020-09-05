nodes = {
    'A' : ['B','C','D'],
    'B' : ['A','C','D'],
    'C' : ['A','B'],
    'D' : ['A','B','E','F'],
    'E' : ['E','F'],
    'F' : ['E','D','G'],
    'G' : ['F']
}
# print(nodes['A'])
# output = {('A','B'):1,('A','C'):1,('C','D'):2}
# print(output[('A','B')])

def bfs_shortest_path(gr,start,end):
    queue_to_store_path =[]
    visited_nodes = set()
    queue_to_store_path.append([start])
    while queue_to_store_path:
        current_path = queue_to_store_path.pop(0)
        last_node_of_current_path =  current_path[-1]
        if last_node_of_current_path == end:
            return current_path
        if last_node_of_current_path not in visited_nodes:
            for node in gr[last_node_of_current_path]:
                new_path = list(current_path)
                new_path.append(node)
                queue_to_store_path.append(new_path)
            visited_nodes.add(node)




def shortest_distance(graph,start_node,end_node) -> int:
    #keep a set of visited nodes
    #use a queue to store the paths
    visited = set()
    path_queue =[[start_node]]
    while path_queue :
        path = path_queue.pop(0)
        vertex = path[-1]
        if vertex == end_node:
            print(path)
            return len(path)-1
        if vertex not in visited:
            for node in graph[vertex]:
                new_path = list(path)
                new_path.append(node)
                path_queue.append(new_path)
            visited.add(vertex)

    return 0





def graph(g,start,end):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == end:
            print(queue)
            return path
        elif vertex not in visited:
            for nodes in g[vertex]:
                new_path = list(path)
                new_path.append(nodes)
                queue.append(new_path)
            visited.add(vertex)


    pass

print(graph(nodes,'C','D'))
print(bfs_shortest_path(nodes,'C','D'))
print(shortest_distance(nodes,'C','K'))
# for nodes
"""
1. what inputs does the function take input
2. is this function going to be called once or multiple times
3. are those nodes part of a tree
4. can we assume the nodes exist in the graph
4. what type of graph is it
5. what does shortest path mean? do the edges of a graph weighted

solution:
use a queue with one of the two nodes as the root
continouosly pop element and add children back into the queue
keep track of distance for each node
return the desired node when found



level order traversal

hashset


"""


