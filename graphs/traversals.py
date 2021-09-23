# depth first and breadth first tree traversals
# depth first, FILO, using list

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def depth_first_recursion(graph, current="a"):
    """Using recursion, which in turn using the call stack."""
    print(current)
    for node in graph.get(current):
        depth_first_recursion(graph, node)


def depth_first_list(graph, current="a"):
    """Using a list as stack."""
    stack = []
    stack.append(current)
    while stack:
        current = stack.pop(-1)
        print(current)
        for node in graph.get(current):
            stack.append(node)


def breadth_first_list(graph, current="a"):
    """Breadth first using a list as queue."""
    queue = []
    queue.append(current)
    while queue:
        current = queue.pop(0)
        print(current)
        for node in graph.get(current):
            queue.append(node)


breadth_first_list(graph, current="a")


def breadth_first(graph, current="a"):
    queue = []
    queue.append(current)
    while queue:
        current = queue.pop()
        for node in graph.get(current):
            queue.append(node)
        current = queue.pop()
