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

    >>> graph = {
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
    ['C', 'A', 'B', 'I']

    """

    D = {} # Final distances dict
    P = {} # Predecessor dict

    # Fill the dicts with default values
    for node in graph.keys():
        D[node] = -1 # Vertices are unreachable
        P[node] = "" # Vertices have no predecessors

    D[start] = 0 # The start vertex needs no move

    unseen_nodes = graph.keys() # All nodes are unseen

    while len(unseen_nodes) > 0:
        # Select the node with the lowest value in D (final distance)
        shortest = None
        node = ''
        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                node = temp_node

        # Remove the selected node from unseen_nodes
        unseen_nodes.remove(node)

        # For each child (ie: connected vertex) of the current node
        for child_node, child_value in graph[node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                # To go to child_node, you have to go through node
                P[child_node] = node

    # Set a clean path
    path = []

    # We begin from the end
    node = end
    # While we are not arrived at the beginning
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node) # Insert the predecessor of the current node
            node = P[node] # The current node becomes its predecessor
        else:
            break

    path.insert(0, start) # Finally, insert the start vertex
    return path


# Create a sample graph and call the function
graph = {   'A':  {'B': 5.9402063753, 'Q': 04.926671928},
            'B':  {'C': 8.7958679374, 'P': 04.435324655},
            'C':  {'D': 9.5304250144, 'O': 06.939517724},
            'D':  {'E': 7.810388475, 'N': 08.443303559},
            'E':  {'M': 08.555273959, 'F': 3.5281374768},
            'F':  {'G': 5.0606564596},
            'G':  {'H': 5.9155801789, 'L': 60.712828614},
            'H':  {'I': 9.1224553311},
            'I':  {'J': 4.9699737349},
            'J':  {'K': 5.8615352385},
            'K':  {'L': 0.1041666667, 'U': 2.555799753},
            'L':  {'M': 1.7595021929},
            'M':  {'N': 2.8862332515, 'Z': 6.3282875344},
            'N':  {'O': 3.9631593723},
            'O':  {'P': 7.5503433873},
            'P':  {'Q': 7.1533978134},
            'Q':  {'R': 8.0438548358},
            'R':  {'Z': 92.949743216, 'S': 4.8729988878},
            'S':  {'Y': 91.417098615},
            'T':  {'X': 15.640600487},
            'U':  {'Z': 22.213072771, 'V': 7.5407012208},
            'V':  {'1': 0.2946414983},
            'W':  {'3': 66.106357967, 'X': 0.7496429414},
            'X':  {'2': 69.733326506, 'Y': 3.3866361649},
            'Y':  {'1': 75.040119719, 'Z': 8.8906828089},
            'Z':  {},
            '1':  {'2': 2.306604772},
            '2':  {'3': 0.327836905},
            '3':  {}
}

result = dijkstra(graph, 'Q', 'T')

print(result)