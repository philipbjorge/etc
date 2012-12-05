import networkx as nx

node_ct = 100
graphs = {
    "Erdos-Renyi P=0.1": nx.erdos_renyi_graph(node_ct, 0.1), 
    "Erdos-Renyi P=0.25": nx.erdos_renyi_graph(node_ct, 0.25), 
    "Erdos-Renyi P=0.5": nx.erdos_renyi_graph(node_ct, 0.5), 
    "Newman-Watts-Strogatz P=0.1, k=10/node_ct": nx.newman_watts_strogatz_graph(node_ct, 10.0/node_ct, 0.1), 
    "Newman-Watts-Strogatz P=0.25, k=10/node_ct": nx.newman_watts_strogatz_graph(node_ct, 10.0/node_ct, 0.25), 
    "Newman-Watts-Strogatz P=0.5, k=10/node_ct": nx.newman_watts_strogatz_graph(node_ct, 10.0/node_ct, 0.5), 
    "Random Regular - Degree=1": nx.random_regular_graph(1, node_ct), 
    "Random Regular - Degree=10": nx.random_regular_graph(10, node_ct), 
    "Random Regular - Degree=50": nx.random_regular_graph(50, node_ct), 
    "Barabasi Albert - Edges=1": nx.barabasi_albert_graph(node_ct, 1),
    "Barabasi Albert - Edges=10": nx.barabasi_albert_graph(node_ct, 10),
    "Barabasi Albert - Edges=50": nx.barabasi_albert_graph(node_ct, 50),
}