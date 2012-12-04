def dijkstra(graph, start, end):

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

    # All nodes are unseen initially
    unseen_nodes = graph.keys()

    while len(unseen_nodes) > 0:
        

        shortest = None
        cur_node = ''

        # Find the node with the shortest distance
        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                cur_node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                cur_node = temp_node

        # Remove the selected node from unseen_nodes
        unseen_nodes.remove(cur_node)

        # For each child of the current node calc the distance
        for child_node, child_value in graph[cur_node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value

                # To go to child_node, you have to go through node
                P[child_node] = cur_node

    # Initialize the path
    path = []

    # Begin from the end
    node = end

    # Search for the start node
    while not (node == start):
        if path.count(node) == 0:
            # Insert the predecessor of the current node
            path.insert(0, node) 

            # The current node becomes its predecessor
            node = P[node]
        else:
            break

    # Finally, insert the start vertex to complete the path
    path.insert(0, start) 
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