from ford_fulkerson import max_flow_and_min_cut 

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 0, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

edge_start, edge_end = 0, 5
print (max_flow_and_min_cut(graph, edge_start, edge_end))