#   https://www.geeksforgeeks.org/saving-a-networkx-graph-in-gexf-format-and-visualize-using-gephi/

import networkx as nx
 
G = nx.path_graph(10)

nx.write_gexf(G, "geeksforgeeks.gexf")
