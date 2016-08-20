#!/usr/bin/env python
# -*- coding: utf8 -*-

from GraphFunctions import *

def main():
    verticesAtivos = np.array([]) #Conjunto de vertices vazio Va(0)
    sementesIniciais = [] #Conjunto de sementes iniciais
    vetorEnergia = np.array([]) #Vetor Energia dos vertices
    #########################################################################################################################
    #Constantes do problema
    limitePrecisao = 0.1 #E0
    limiteInferior = 0.1 #Threshold
    espalhamentoGlobal = 0.8 #Beta
    communityGraphs = []

    # Iniciar o grafo.
    g = Graph.Read_Ncol(sys.argv[1],names = True,weights = "if_present",directed = False)
    g.simplify(combine_edges = "sum")
    x = g.community_multilevel(weights = "weight")
    for graph in x:
        communityGraphs.append(Graph.subgraph(g,graph))
        


if __name__ == "__main__" : main()
