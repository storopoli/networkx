import networkx as nx

# DOT Layout
nx.nx_pydot.graphviz_layout(G)
nx.nx_agraph.graphviz_layout(G)

# Gephi gexf file
nx.write_gexf(G, 'file.gexf')

# Pajek net file
nx.write_pajek(G, 'file.net')