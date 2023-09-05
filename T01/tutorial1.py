graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from priority_queue import PriorityQueue
from collections import defaultdict

def tree_search(graph, initial_node, goal_test, is_update):
    frontier = PriorityQueue('min')
    frontier.append(0, initial_node)
    while frontier.__len__() != 0:
         current_node = frontier.pop()
         print(current_node)
         if (goal_test(current_node[1])):
             return 
         for val in graph.get(current_node[1]):
               newVal = val[1] + current_node[0]
               frontier.append(newVal, val[0])
         frontier.print()
    return

def graph_search(graph, initial_node, goal_test, is_update):
    frontier = PriorityQueue('min')
    visited = {initial_node}
    frontier.append(0, initial_node)
    while frontier.__len__() != 0:
         current_node = frontier.pop()
         print(current_node)
         visited.add(current_node[1])
         if (goal_test(current_node[1])):
             return 
         for val in graph.get(current_node[1]):
               newVal = val[1] + current_node[0]
               if not val[0] in visited:   
                 frontier.append(newVal, val[0])
         frontier.print()
    return

# Return the path found
def uniform_cost_search(graph, initial_node, goal_test, is_tree, is_update):
    if is_tree:
        tree_search(graph, initial_node, goal_test, is_update)
    else:
        graph_search(graph, initial_node, goal_test, is_update)



print("=====")
print("Tree")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False))

print("=====")
print("Graph")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True))
