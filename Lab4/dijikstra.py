from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def add_node(self,value):
        self.nodes.add(value)
    
    def add_edge(self, edge_start, edge_end, distance):
        self.edges[edge_start].append(edge_end)
        self.distances[(edge_start, edge_end)] = distance

def dijkstra(graph, initial_value):
        vertexes = {initial_value : 0}
        path = defaultdict(list)
        nodes = set(graph.nodes)

        while nodes:
            smallest_node = None
            for node in nodes:
                if node in vertexes:
                    if smallest_node is None:
                        smallest_node = node
                    elif vertexes[node] < vertexes[smallest_node]:
                        smallest_node = node
            if smallest_node is None:
                break

            nodes.remove(smallest_node)
            current_distance = vertexes[smallest_node]

            for edge in graph.edges[smallest_node]:
                distance = current_distance + graph.distances[(smallest_node, edge)]
                if edge not in vertexes or distance < vertexes[edge]:
                    vertexes[edge] = distance
                    path[edge].append(smallest_node)

        list_of_average_distance = []
        for i in vertexes:
            list_of_average_distance.append(vertexes[i])
            final = sum(list_of_average_distance)
        len_of_list = len(vertexes)
        print(final/(len_of_list-1))

        return vertexes   