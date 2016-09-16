#!/usr/bin/env python
# -*- coding: utf8 -*-
from GraphFunctions import *

class CommunityGraphs:
    _communityGraphs = []
    _vGrau = 0
    _vPageRank = 0



def main():
    verticesAtivos = np.array([]) #Conjunto de vertices vazio Va(0)
    sementesIniciais = [] #Conjunto de sementes iniciais
    vetorEnergia = np.array([]) #Vetor Energia dos vertices
    #Constantes do problema
    limitePrecisao = 0.1 #E0
    limiteInferior = 0.1 #Threshold
    espalhamentoGlobal = 0.8 #Beta
    communityGraphs = [] #Lista de grafos
    #Matriz W

    # Iniciar o grafo.
    try:
        g = Graph.Read_Ncol(sys.argv[1],names = True,weights = "if_present",directed = False)
        g.vs['name'] = [v.index for v in g.vs()]
    except IOError as err:
        print err
    else:
        g.simplify(combine_edges = "sum")
        graphList = g.community_multilevel(weights = "weight")
        # Lista de comunidades, que e uma classe que contém as caracteristicas de cada comunidade que serão
        # utilizadas para comparar as comunidades
        communityGraphs= [ CommunityGraphs() for graph in graphList ]
        for graph in graphList:
            CommunityGraphs._communityGraphs.append(Graph.subgraph(g,graph))
        #Grau e PageRank do grafo completo
        vGrau,vPageRank = vCaracteristicas(g)
        # Adiciona o vetor ordenado decrescente, em grau e page rank, a cada comunidade.
        listW = []
        i = 0
        for graphs in CommunityGraphs._communityGraphs:
            W = np.zeros((graphs.vcount(),graphs.vcount()),dtype = np.float32)#Inicializa uma matriz de pesos
            graphs.vs['name'] = [v.index for v in g.vs()]
            print("--------------Obtendo W------------------")
            listW.append(obterMatrizW(W,graphs,0))

        #i=0
        #for graphs in CommunityGraphs._communityGraphs:
            communityGraphs[i]._vGrau , communityGraphs[i]._vPageRank = vCaracteristicas(graphs)
        #    i = i + 1
        #i = 0
        #for graphs in CommunityGraphs._communityGraphs:
            tamSementesIniciais = int(len(communityGraphs[i]._vGrau)*0.9)
            sementesIniciais = communityGraphs[i]._vGrau[0:tamSementesIniciais]
            verticesAtivos = obterSementesIniciais(graphs,sementesIniciais,graphs.vcount())
            vetorEnergia = obterVetorEnergia(graphs,sementesIniciais,graphs.vcount())
            print("--------------Operacao de Energia--------------")
            operacaoEnergia(graphs,verticesAtivos,vetorEnergia,espalhamentoGlobal,listW[i],graphs.vcount(),limitePrecisao,limiteInferior)
            print("Quantidade de vertices Ativos : " +  str(len(verticesAtivos)) + "\n")
            print("Quantidade de vertices Ativos : " +  str(len(sementesIniciais)) + "\n")
            i = i + 1

        # tamanhoSementesIniciais = int(len(vGrau)*float(sys.argv[3]))
        # sementesIniciais = vGrau[0:tamanhoSementesIniciais]
        # file2 = open('Grau/SementesIniciais/SementesIniciaisGrau.txt','a')
        # file2.writelines(str(float(sys.argv[3])*100)+"%"+" "+ str(sementesIniciais[:]) + "\n")
        # verticesAtivos = obterSementesIniciais(g,sementesIniciais,NUMVERT)
        # vetorEnergia = obterVetorEnergia(g,sementesIniciais,NUMVERT)
        # print("--------------Operacao de Energia--------------")
        # operacaoEnergia(g,verticesAtivos,vetorEnergia,espalhamentoGlobal,W,NUMVERT,limitePrecisao,limiteInferior)
        # print("Quantidade de vertices Ativos : " +  str(len(verticesAtivos)) + "\n")
        # print("Quantidade de Sementes Iniciais: " + str(len(sementesIniciais)))
        # print "--------------Plot SubGrafo ----------- \n"
        # f = open('Grau/Tempo/TempoGrau.txt', 'a')
        # f.writelines(str(float(sys.argv[3])*100)+ "%" + " " + str(len(verticesAtivos)) + " " + str(len(sementesIniciais))+"\n")
        # print "Tempo: ",time()-t
        # print montarSubGrafo(g,verticesAtivos).summary()
        # plot(montarSubGrafo(g,verticesAtivos),"subGrafoGrau" + sys.argv[3] + ".png",layout = "circle")



        # Procura o atributo 'name' no grafo original e acha o index do vertice.
        #   for v in g.vs():
        #        if v['name'] == '36':
        #            print v
        #
        # Todo Grafo tem um nome, pode usa-lo para relacionar os vertices dos grafos comunidade com o grafo original
        # print CommunityGraphs._communityGraphs[0].vs[0]['name']
        # Escolha das sementes iniciais utilizando Page Rank e Grau. (Falta Random)
        # Print os maiors pageRanks e Grau de todos os grafos.
        #
        # print "Grafo :" + str(vGrau[0]) + " " + str(vPageRank[0])
        # print "Grafo Comunidade 1: " + str(communityGraphs[0]._vGrau) + " " + str(communityGraphs[0]._vPageRank[0])
        # print "Grafo Comunidade 2: " + str(communityGraphs[1]._vGrau) + " " + str(communityGraphs[1]._vPageRank[0])
        # print "Grafo Comunidade 3: " + str(communityGraphs[2]._vGrau) + " " + str(communityGraphs[2]._vPageRank[0])
        #
        # Rodar o algoritmo de Spreading Activation para cada comunidade.
        # Comparar os maiores Page Rank(Grau) de cada comunidade.
        # Ver qual comunidade irá difundir mais a energia.


if __name__ == "__main__" : main()
