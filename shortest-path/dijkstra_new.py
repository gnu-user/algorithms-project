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

"""
testcase1:
['C', 'D', 'E', 'F', 'G', 'H', 'I']
(161.21066997518614, 396.77518610421834)
(208.86458333333331, 383.27083333333326)
(263.70833333333326, 364.98958333333326)
(280.63541666666663, 415.77083333333326)
(333.44791666666663, 400.1979166666666)
(357.82291666666663, 391.39583333333326)
(385.58333333333326, 382.5937499999999)

testcase 2:
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
(70.4712158808933, 423.99702233250616)
(114.54466501240695, 411.0342431761786)
(161.21066997518614, 396.77518610421834)
(208.86458333333331, 383.27083333333326)
(263.70833333333326, 364.98958333333326)
(280.63541666666663, 415.77083333333326)
(333.44791666666663, 400.1979166666666)
(357.82291666666663, 391.39583333333326)
(385.58333333333326, 382.5937499999999)
(363.91666666666663, 310.82291666666663)

testcase3:
['Q', 'R', 'S', 'T']
(37.5625, 324.36458333333326)
(20.635416666666686, 268.84374999999994)
(5.739583333333343, 216.03124999999994)
(187.19791666666663, 155.09375)

testcase4:
['A', 'B', 'C', 'O']
(70.4712158808933, 423.99702233250616)
(114.54466501240695, 411.0342431761786)
(161.21066997518614, 396.77518610421834)
(127.61458333333331, 295.24999999999994)
"""