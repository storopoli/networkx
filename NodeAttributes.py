import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# fator dictionary
factor_dict = {
    "bc1": 1,
    "bc2": 2,
}

# also you can create from a pandas series and index
factor_dict = pd.Series(factor.ID.values, index=factor.node).to_dict()

# set node attribute by a dictionary
nx.set_node_attributes(G, factor_dict, name='fator')

# Remove nodes without fator
selected_nodes = [i for i in list(G.nodes) if i in list(factor_dict.keys())]
removed_nodes = [i for i in list(G.nodes) if i not in list(factor_dict.keys())]
G.remove_nodes_from(removed_nodes)

# Creating several subnetworks for every fator as subgraph_1 etc.
for i in set(factor_dict.values()):
    sub_selected_nodes = [n for n,v in G.nodes(data=True) if v['fator'] == i]
# You can create global variable for each subgrapg
    globals()[f"subgraph_{i}"] = G.subgraph(sub_selected_nodes)
    globals()[f"subgraph_{i}"].name = f"Fator {i}"
# Printing Sub Graph Info and Density
    print(f"Info for factor {i} is", nx.info(G.subgraph(sub_selected_nodes)))
    print(f"Density for factor {i} is", nx.density(G.subgraph(sub_selected_nodes)))
# Use the function getCentralization.py to get Network Centralization
    print(f"Centralization for factor {i} is", getCentralization(nx.degree_centrality(G.subgraph(sub_selected_nodes)), c_type="degree"))
# Also save a plot
    nx.draw_networkx(G.subgraph(sub_selected_nodes), with_labels=True, fontsize=0.0001, node_size=100, arrow_size=10, width=1)
    plt.savefig(f"Fator {i}.png", dpi=200)
