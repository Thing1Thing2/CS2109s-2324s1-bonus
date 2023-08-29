graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from priority_queue import PriorityQueue
from collections import defaultdict

def uniform_cost_search(graph, inital_node, goal_test, is_tree, is_update):

    # frontier = PriorityQueue('min', f)
    raise NotImplementedError

print("=====")
print("Tree")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False))
assert(p=="SASASBSBG")
# You might get a different path due to popping of B instead.
# A(5) B(5) B(7) B(9) G(11) G(13) C(15) C(17) C(19)

print("=====")
print("Graph")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True))
assert(p=="SBG")