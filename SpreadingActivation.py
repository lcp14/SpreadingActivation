#!/usr/bin/env python
# -*- coding: utf8 -*-

from GraphFunctions import *

# Main
def main():
    #arq = open('InitialSeeds.txt','r')
    #########################################################################################################################
    # Declaração de variaveis
    verticesAtivos = np.array([]) #Conjunto de vertices vazio Va(0)
    sementesIniciais = [] #Conjunto de sementes iniciais
    vetorEnergia = np.array([]) #Vetor Energia dos vertices
    #########################################################################################################################
    #Constantes do problema
    limitePrecisao = 0.1 #E0
    limiteInferior = 0.1 #Threshold
    espalhamentoGlobal = 0.8 #Beta
    #########################################################################################################################
    #Flags
    flagOpt = 0
    value = True
    #########################################################################################################################
    # Função converter String to booleano
    value = parseBoolString(sys.argv[2])
    #########################################################################################################################
    # Criação do grafo
    g = Graph.Read_Ncol(sys.argv[1],names = True,weights = "if_presente",directed = value)
    g.vs['name'] = [v.index for v in g.vs()]
    #g.simplify(combine_edges=dict(weight="sum"))
    NUMVERT = g.vcount()
    # Mostrar na tela os detalhes do grafo
    print(g.summary())
    #########################################################################################################################
    # miniMenu escolha se é direcionado ou não, e qual operação usar.
    #########################################################################################################################
    W = np.zeros((NUMVERT,NUMVERT),dtype = np.float32)#Inicializa uma matriz de pesos
    if (g.is_directed() == True):
        print("0 - All")
        print("1 - In")
        print("2 - Out")
        flagOpt = int (raw_input("Escolha a opcao: "))
    #########################################################################################################################
    #Começando as operações no grafo.
    t = time()
    print("--------------Obtendo W------------------")
    W = obterMatrizW(W,g,flagOpt)
    #print(W)
    print("--------------Escolhendo Sementes Iniciais---------------")
    vGrau,vPageRank = vCaracteristicas(g)
    #########################################################################################################################
    # Escolhendo as sementes iniciais de acordo com a lista ordenada do PageRank. Para trocar a quantidade de sementes basta alterar
    # o valor de 0.5 para outro valor. Os valores que serão testados são 0.005 (0.5%),0.01(1%),0.05 (5%),0.1 (10%)
    ######################################################################################################################
    # Tipos de operação: 0 Random ; 1 Grau ; 2 Page Rank;

    ######################################################################################################################
    ############################# Usando Random #########################################################################
    if int(sys.argv[4]) == 0 :
        tamanhoSementesIniciais = int(len(g.vs())*float(sys.argv[3]))
        sementesIniciais = random.sample([v.index for v in g.vs()],tamanhoSementesIniciais)
        file2 = open('Random/SementesIniciais/SementesIniciaisRandom.txt','a')
        file2.writelines(str(float(sys.argv[3])*100)+" %"+" "+ str(sementesIniciais[:]) + "\n")
        verticesAtivos = obterSementesIniciais(g,sementesIniciais,NUMVERT)
        vetorEnergia = obterVetorEnergia(g,sementesIniciais,NUMVERT)
        print("--------------Operacao de Energia--------------")
        operacaoEnergia(g,verticesAtivos,vetorEnergia,espalhamentoGlobal,W,NUMVERT,limitePrecisao,limiteInferior)
        print("Quantidade de vertices Ativos : " +  str(len(verticesAtivos)) + "\n")
        print("Quantidade de Sementes Iniciais: " + str(len(sementesIniciais)))
        print "--------------Plot SubGrafo ----------- \n"
        f = open('Random/Tempo/TempoRandom.txt', 'a')
        f.writelines(str(float(sys.argv[3])*100)+ "%" + " " + str(len(verticesAtivos)) + " " + str(len(sementesIniciais))+"\n")
        print "Tempo: ",time()-t
        print montarSubGrafo(g,verticesAtivos).summary()
        plot(montarSubGrafo(g,verticesAtivos),"subGrafoRandom" + sys.argv[3] + ".png",layout = "circle")
    ######################################################################################################################

    ######################################################################################################################
    ############################ Usando Grau do vertice ####################################
    if int(sys.argv[4]) == 1 :
        tamanhoSementesIniciais = int(len(vGrau)*float(sys.argv[3]))
        sementesIniciais = vGrau[0:tamanhoSementesIniciais]
        file2 = open('Grau/SementesIniciais/SementesIniciaisGrau.txt','a')
        file2.writelines(str(float(sys.argv[3])*100)+"%"+" "+ str(sementesIniciais[:]) + "\n")
        verticesAtivos = obterSementesIniciais(g,sementesIniciais,NUMVERT)
        vetorEnergia = obterVetorEnergia(g,sementesIniciais,NUMVERT)
        print("--------------Operacao de Energia--------------")
        operacaoEnergia(g,verticesAtivos,vetorEnergia,espalhamentoGlobal,W,NUMVERT,limitePrecisao,limiteInferior)
        print("Quantidade de vertices Ativos : " +  str(len(verticesAtivos)) + "\n")
        print("Quantidade de Sementes Iniciais: " + str(len(sementesIniciais)))
        print "--------------Plot SubGrafo ----------- \n"
        f = open('Grau/Tempo/TempoGrau.txt', 'a')
        f.writelines(str(float(sys.argv[3])*100)+ "%" + " " + str(len(verticesAtivos)) + " " + str(len(sementesIniciais))+"\n")
        print "Tempo: ",time()-t
        print montarSubGrafo(g,verticesAtivos).summary()
        plot(montarSubGrafo(g,verticesAtivos),"subGrafoGrau" + sys.argv[3] + ".png",layout = "circle")
        ######################################################################################################################

        ######################################################################################################################
        ############################### Usando Page Rank #########################################
    if int(sys.argv[4]) == 2 :
        tamanhoSementesIniciais = int(len(vPageRank)*float(sys.argv[3]))
        sementesIniciais = vGrau[0:tamanhoSementesIniciais]
        file2 = open('PageRank/SementesIniciais/SementesIniciaisPageRank.txt','a')
        file2.writelines(str(float(sys.argv[3])*100)+"%"+" "+ str(sementesIniciais[:]) + "\n")
        verticesAtivos = obterSementesIniciais(g,sementesIniciais,NUMVERT)
        vetorEnergia = obterVetorEnergia(g,sementesIniciais,NUMVERT)
        print("--------------Operacao de Energia--------------")
        operacaoEnergia(g,verticesAtivos,vetorEnergia,espalhamentoGlobal,W,NUMVERT,limitePrecisao,limiteInferior)
        print("Quantidade de vertices Ativos : " +  str(len(verticesAtivos)) + "\n")
        print("Quantidade de Sementes Iniciais: " + str(len(sementesIniciais)))
        print "--------------Plot SubGrafo ----------- \n"
        f = open('PageRank/Tempo/TempoPageRank.txt', 'a')
        f.writelines(str(float(sys.argv[3])*100)+ "%" + " " + str(len(verticesAtivos)) + " " + str(len(sementesIniciais))+"\n")
        print "Tempo: ",time()-t
        print montarSubGrafo(g,verticesAtivos).summary()
        plot(montarSubGrafo(g,verticesAtivos),'subGrafoPageRank' + sys.argv[3] + '.png',layout = "circle")

    ######################################################################################################################

    ######################################################################################################################
    #list.sort(aux)
    #print vPageRank,"\n",g.vs[vPageRank[0]].index
    #print g.summary()
    #print(vPageRank)
    ######################################################################################################################




    #g.simplify()
    #plot(g,"grafoOriginal.png",layout = "rt")
    #print("Tempo Total:")
    #print(time()-t)

if __name__ == "__main__": main()
