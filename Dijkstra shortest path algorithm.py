#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:25:52 2021

@author: raphaelmunoz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:25:09 2021

@author: raphaelmunoz

Graph

              (a)
          ⁄/\ /|\  \
          /    |    \ 1
      6  /     |     \
        /      |     _\⁄ 
(start)        |      (fin)
               |3
        \      |     ⁄/\
         \     |     / 5
       2  \    |    /
           \   |   /
             _\ \/_
              (b)

"""

# INPUT: Add the Nodes in graph

graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a':3, 'fin': 5}, 'fin': {}}

infinity = float("inf")

# INPUT Add the costs

costs = {'a': 6, 'b': 2, 'fin': infinity}

# INPUT Add a known parents. Insert None for unknown

parents = {'a': 'start', 'b': 'start', 'fin': None}

processed = []
nodes = []

def find_the_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
        
        
node = find_the_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_the_lowest_cost_node(costs)

    if node is not None:
        nodes.append(node)
        
print("The nodes processed were:  {}".format(processed))
print("The lowest path nodes were: {}".format(nodes))
print("The cost is: {}".format(cost))