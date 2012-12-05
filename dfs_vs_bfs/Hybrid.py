from collections import deque

def hybrid_edges(g, source, dfs=False):
    # Hybrid DFS/BFS
    visited = set([source])
    stack = [(source,iter(g[source]))]
    deq = deque(stack)
    while len(deq):
        if dfs:
            parent, children = deq[0]
        else:
            parent, children = deq[-1]

        try:
            child = next(children)
            if child not in visited:
                yield parent,child
                visited.add(child)
                deq.append((child,iter(g[child])))
        except StopIteration:
            if dfs:
                deq.popLeft()
            else:
                deq.pop()
