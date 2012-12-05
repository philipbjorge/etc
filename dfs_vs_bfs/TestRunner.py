import networkx as nx
import random
from TestCases import *
from Hybrid import *

test_count = 500

for (name, G) in graphs.iteritems():
    # Filename = algorithm_safename.data
    # Format = 1st line: title, 2nd line: algorithm, 3rd line: node count, all else is time to node
    safe_name = "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    # 1. DFS
    with open("dfs_" + safe_name + ".data", 'w') as f:
        f.write(name + "\n")
        f.write("DFS\n")
        f.write(str(node_ct) + "\n")
        for i in xrange(test_count):
            # Init
            start = random.randint(0, node_ct - 1)
            target = random.randint(0, node_ct - 1)
            edge_traversal_ct = 0
            g = G()

            # Search
            for (e_s, e_t) in nx.dfs_edges(g, source=start):
                edge_traversal_ct += 1
                if e_s is target or e_t is target:
                    break

            # Output
            f.write("%d\n" % edge_traversal_ct)

    # 2. BFS
    with open("bfs_" + safe_name + ".data", 'w') as f:
        f.write(name + "\n")
        f.write("BFS\n")
        f.write(str(node_ct) + "\n")
        for i in xrange(test_count):
            # Init
            start = random.randint(0, node_ct - 1)
            target = random.randint(0, node_ct - 1)
            edge_traversal_ct = 0
            g = G()

            # Search
            for (e_s, e_t) in nx.bfs_edges(g, source=start):
                edge_traversal_ct += 1
                if e_s is target or e_t is target:
                    break

            # Output
            f.write("%d\n" % edge_traversal_ct)

    # 3. DFS/BFS with the possibility of changing strategies of probability p at any given node
    with open("hybrid_" + safe_name + ".data", 'w') as f:
        f.write(name + "\n")
        f.write("Hybrid\n")
        f.write(str(node_ct) + "\n")
        for i in xrange(test_count):
            # Init
            start = random.randint(0, node_ct - 1)
            target = random.randint(0, node_ct - 1)
            edge_traversal_ct = 0
            g = G()

            # Search
            tech = False
            for (e_s, e_t) in hybrid_edges(g, start, tech):
                edge_traversal_ct += 1
                if e_s is target or e_t is target:
                    break

                if random.random() < 0.5:
                    # Switch techniques
                    tech = not tech

            # Output
            f.write("%d\n" % edge_traversal_ct)
