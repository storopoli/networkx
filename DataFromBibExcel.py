import pandas as pd
import networkx as nx

# adjacency matrix from BibExcel
df = pd.read_csv('filename.csv', sep=';', index_col=0)
G = nx.from_pandas_adjacency(df)
G.name = 'Name'
print(nx.info(G))
