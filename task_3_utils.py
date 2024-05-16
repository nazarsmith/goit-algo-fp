import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class GraphWorkshop:
    def __init__(self, nodes: dict):
        self.nodes = nodes

        _ = plt.figure(figsize = (10,10))

    def construct_undirected_graph(self):
        self.un_G = nx.Graph()
        for k,v in self.nodes.items():
            [self.un_G.add_edge(k, node, weight = len(v) / 2) for node in v]
    
    def construct_directed_graph(self, label = None):
        if label:
            self.res_G = nx.DiGraph()
        else:
            self.dir_G = nx.DiGraph()
            for k,v in self.nodes.items():
                [self.dir_G.add_edge(k, node, weight = len(v) / 2) for node in v]
    
    def get_graph_properties(self, graph: nx.Graph|nx.DiGraph):

        props = {
            "pos" : nx.kamada_kawai_layout(graph),
            "edges" : graph.edges(),
            "nodes" : graph.nodes(),
            "weights" : [graph[u][v]['weight'] for u,v in graph.edges()],
            "closensess" : nx.closeness_centrality(graph),
            "betweenness" : nx.betweenness_centrality(graph),
            "leaf_nodes" : [
                node for node in graph.nodes() if (
                    graph.degree(node) <= 1
                )
            ]
        }    
        return props
    
    def draw_graph(self, graph: nx.Graph|nx.DiGraph):
        properties = self.get_graph_properties(graph)
        nx.draw(graph, pos = properties["pos"], with_labels = True, width = properties["weights"])
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos = properties["pos"], edge_labels=labels)
        return properties
    
    def show_graph(self):
        plt.show()
    
    def aggregate_properties(self, graph: nx.Graph|nx.DiGraph, properties: dict):

        nodes_properties = {}
        for n in properties["nodes"]:
            nodes_properties.update(
                {
                    n: {
                        "degree_centrality": graph.degree(n),
                        "closeness_centrality": properties["closensess"][n],
                        "betweenness_centrality": properties["betweenness"][n],
                    }
                }
            )
        n_props = pd.DataFrame.from_dict(nodes_properties)

        is_connected = nx.is_connected(graph) if not graph.is_directed() else "N/A"
        graph_properties = {
            "Graph" : {
                "Number of nodes": len(properties["nodes"]),
                "Number of edges:": len(properties["edges"]),
                "Graph is connected": is_connected,
                "Average node degree": n_props.loc["degree_centrality"].mean()
            }
        }
        g_props = pd.DataFrame.from_dict(graph_properties)

        return n_props, g_props
    
    def bfs(self, graph, start):
        bfs_tree = nx.bfs_tree(graph, start)
        return bfs_tree

    def dfs(self, graph, start):
        dfs_tree = nx.dfs_tree(graph, start)
        return dfs_tree
    
    def dij(self, graph, source, target):
        return nx.dijkstra_path(graph, source, target)
    
    def draw_dbfs_tree(self, edges: tuple[list]):
        _ = plt.figure(figsize = (10,10))
        self.construct_directed_graph(label = "result")
        result_tree = self.res_G
        result_tree.add_edges_from(edges)
        pos = nx.planar_layout(result_tree)
        nx.draw(result_tree, pos = pos, with_labels = True)
        plt.show()

if __name__ == "__main__":
    nodes = {
            "A": ["LT", "H2", "CM2", "A1"],
            "A1": ["A", "A2", "H3"],
            "A2": ["A1", "S3"],
            "B": ["TH1", "TH2"],
            "T": ["M"],
            "M": ["T", "CH", "C"],
            "C": ["M", "C1", "TH2", "P"],
            "C1": ["C", "CH", "CM2"],
            "P": ["C", "LT", "P1"],
            "P1": ["P"],
            "LT": ["P", "A", "S"],
            "S": ["LT", "S1", "S2"],
            "S1": ["S", "S4", "R2"],
            "S2": ["S1", "S", "S3", "R1"],
            "S3": ["DE", "A2", "S2"],
            "S4": ["S1", "I"],
            "R1": ["CR", "R2", "S2"],
            "R2": ["S1", "R1"],
            "H1": ["CM", "H2"],
            "H2": ["H1", "A"],
            "H3": ["A1"],
            "DE":["S3"],
            "I": ["TH2", "S4"],
            "TH1": ["B", "M"],
            "TH2": ["B", "TH1", "I"],
            "CM1": ["CH", "CM2"],
            "CM2": ["CM1", "A", "C1", "RD", "H1"],
            "RD": ["CM2"],
            "CR": [],
            "CH": ["M", "CM1"]
        }
    
    graph_workshop = GraphWorkshop(nodes)

    graph_workshop.construct_undirected_graph()
    un_graph = graph_workshop.un_G
    
    graph_workshop.draw_graph(un_graph)
    un_graph_props = graph_workshop.get_graph_properties(un_graph)
    nodes, graph = graph_workshop.aggregate_properties(un_graph, un_graph_props)
    print(nodes, graph)
    graph_workshop.show_graph()