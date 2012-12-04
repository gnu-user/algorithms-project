#import pdb; pdb.set_trace()
def dijkstra(graph, start, end):
    """
    Dijkstra's algorithm Python implementation.

    Arguments:
        graph: Dictionnary of dictionnary (keys are vertices).
        start: Start vertex.
        end: End vertex.

    Output:
        List of vertices from the beggining to the end.

    Example:

    graph = {
    ...     'A': {'B': 10, 'D': 4, 'F': 10},
    ...     'B': {'E': 5, 'J': 10, 'I': 17},
    ...     'C': {'A': 4, 'D': 10, 'E': 16},
    ...     'D': {'F': 12, 'G': 21},
    ...     'E': {'G': 4},
    ...     'F': {'H': 3},
    ...     'G': {'J': 3},
    ...     'H': {'G': 3, 'J': 5},
    ...     'I': {},
    ...     'J': {'I': 8},
    ... }    
    >>> dijkstra(graph, 'C', 'I')
    ['C', 'A', 'B', 'I']"""

    # Final distances dict
    D = {}

    # Predecessor dict
    P = {} 

    # Fill the dicts with default values
    for node in graph.keys():
        D[node] = -1 # Vertices are unreachable
        P[node] = "" # Vertices have no predecessors

    # The start vertex does not need to move and is reachable
    D[start] = 0 

    # All nodes are unseen
    unseen_nodes = graph.keys()

    while len(unseen_nodes) > 0:
        # Select the node with the lowest value in D (final distance)
        shortest = None
        cur_node = ''
        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                cur_node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                cur_node = temp_node

        # Remove the selected node from unseen_nodes
        unseen_nodes.remove(cur_node)

        # For each child (ie: connected vertex) of the current node
        for child_node, child_value in graph[cur_node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                # To go to child_node, you have to go through node
                P[child_node] = cur_node

    # Initialize the path
    path = []

    # Begin from the end
    node = end

    # While the current node is not the start node
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node) # Insert the predecessor of the current node
            node = P[node] # The current node becomes its predecessor
        else:
            break

    path.insert(0, start) # Finally, insert the start vertex
    return path


# Create a sample graph and call the function


graph = {   'A' : {'B': 46, 'Q': 105},
            'B' : {'C': 49, 'P': 104},
            'C' : {'D': 50, 'O': 107},
            'D' : {'E': 58, 'N': 108},
            'E' : {'M': 109, 'F': 54},
            'F' : {'G': 55},
            'G' : {'H': 26, 'L': 161},
            'H' : {'I': 29},
            'I' : {'J': 75},
            'J' : {'K': 86},
            'K' : {'L': 50, 'V': 53},
            'L' : {'M': 62},
            'M' : {'N': 53, 'U': 56},
            'N' : {'O': 54},
            'O' : {'P': 48},
            'P' : {'Q': 47},
            'Q' : {'R': 58},
            'R' : {'U': 193, 'S': 55},
            'S' : {'T': 191},
            'T' : {'X': 175, 'U': 59, '2': 53},
            'U' : {'V': 122},
            'V' : {'W': 48},
            'W' : {'X': 60},
            'X' : {'Y': 52},
            'Y' : {'Z': 50},
            'Z' : {'1': 166},
            '1' : {'2': 51},
            '2' : {'Y': 170},
            '3' : {'2': 116}
}


result = dijkstra(graph, 'A', 'O')

    
#result = dijkstra(graph, 'T', 'M')

print(result)
#test case 1: ['C', 'D', 'E', 'F', 'G', 'H', 'I'] Given: C and I 
#test case 2: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] Given A and J
#test case 3: ['Q', 'R', 'S', 'T'] Given Q and T
#test case 4: ['A', 'B', 'C', 'O'] Given A and O