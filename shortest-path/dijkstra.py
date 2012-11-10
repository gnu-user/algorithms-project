def dijkstra(graph, source):
#    for each vertex v in Graph:                                # Initializations
#        dist[v] = infinity                                     # Unknown distance function from 
#                                                               # source to v
#		  previous[v] = undefined                               # Previous node in optimal path
#                                                               # from source
#
#    dist[source] = 0                                           # Distance from source to source
#    Q  = the set of all nodes in Graph                         # All nodes in the graph are
#                                                               # unoptimized - thus are in Q
#    while Q is not empty:                                      # The main loop
#        u = vertex in Q with smallest distance in dist[]       # Start node in first case
#        remove u from Q
#        if dist[u] = infinity: 
#            break                                              # all remaining vertices are
#                                                               # inaccessible from source
#          
#        for each neighbor v of u:                              # where v has not yet been 
#                                                               # removed from Q.
#            alt := dist[u] + dist_between(u, v)   
#            if alt < dist[v]:                                  # Relax (u,v,a)
#                dist[v] = alt  
#                previous[v] = u  
#                decrease-key v in Q                            # Reorder v in the Queue
#    return dist;