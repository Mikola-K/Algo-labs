def dfs(graph, max_flow, edge_start, edge_end):
        visited = [edge_start]
        paths={edge_start:[]}
        if edge_start == edge_end:
                return paths[edge_start]
        while(visited):
                u = visited.pop()
                for ind in range(len(graph)):
                        if(graph[u][ind] - max_flow[u][ind] > 0) and ind not in paths:
                                paths[ind] = paths[u]+[(u,ind)]
                                if ind == edge_end:
                                        return paths[ind]
                                visited.append(ind)
        return None

def max_flow_and_min_cut(graph, edge_start, edge_end):
        node = len(graph)
        max_flow = [[0] * node for i in range(node)]
        path_flow = dfs(graph, max_flow, edge_start, edge_end)
        while path_flow != None:
            flow = min(graph[u][ind] - max_flow[u][ind] for u, ind in path_flow)
            for u,v in path_flow:
                max_flow[u][v] += flow
                max_flow[v][u] -= flow
            path_flow = dfs(graph,max_flow,edge_start,edge_end)
        return sum(max_flow[edge_start][i] for i in range(node))