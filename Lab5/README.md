# Algo labs 5

## Task:
    Implement a min-cut in graph
## Complexity
- Worst case time complexity: Θ(max_flow * E)
- Space complexity: Θ(E + V)

## Algorithm
The Ford-Fulkerson algorithm is based on the three important concepts: the residual network augmented path and cut.

The max-flow min-cut theorem states that the maximum flow through any network from a given source to a given sink is exactly equal to the minimum sum of a cut. This theorem can be verified using the Ford-Fulkerson algorithm. This algorithm finds the maximum flow of a network or graph.

In general, a cut is a set of edges whose removal divides a connected graph into two disjoint subsets.

The minimum cut of a weighted graph is defined as the minimum sum of weights of edges that, when removed from the graph, divide the graph into two sets.

The throughput of the section is the sum of the capacity of the arcs included in the section.

According to this theorem, we can construct and consider all sections and find the minimum - this is the maximum bandwidth of a given network. But from this theorem we cannot find all flows passing through the arcs of the network. Marks are used to indicate the magnitude of the flow and its source.

The flow in each direct arc increases, it should not exceed its capacity, and the flow in each reverse arc decreases, but it should not become negative.

## How to run:
- cd into folder where you want to store this repository
- Clone this repository with command git clone https://github.com/Mikola-K/Algo-labs.git
- Choose branch lab5 with command git checkout lab5
- Go into folder with files with command cd Algo-labs/lab5
- run command python3 -m unittest test.py on Mac/Linux or py -m unittest test.py on Windows