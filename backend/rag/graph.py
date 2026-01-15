graph = {}

def add_relation(a, b):
    graph.setdefault(a, set()).add(b)

def neighbors(node):
    return list(graph.get(node, []))
