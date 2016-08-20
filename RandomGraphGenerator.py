#!/usr/bin/env python
from igraph import *
import numpy as np
import sys
def generateRandomWeightedGraph(V,E,D,minW,maxW):
    g = Graph.Barabasi(V,E,directed = D, implementation = "psumtree")
    g.vs['name'] = [v.index for v in g.vs()]
    for e in g.es:
        e['weight'] = np.random.randint(minW,maxW)
    return g
def main():
    #g = generateRandomWeightedGraph(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    #g = Graph.Barabasi(5000,1000,directed = True, implementation = "psumtree")
    g = Graph.Read_GML("Grafos/as-22july06/as-22july06.gml")
    #g = Graph.Famous("Krackhardt_Kite")
    g.vs['name'] = [v.index for v in g.vs()]
    for e in g.es:
        e['weight'] = np.random.randint(1,10)
    g.write_ncol('grafo_as-22july06.txt',names = "name",weights = "weight")
    g = Graph.Read_Ncol('pqp.txt',names = True,weights = "if_presente",directed = False)
    print g

if __name__ == "__main__" : main()
