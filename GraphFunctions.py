#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *
import sys
import numpy as np
import random
from scipy.sparse import csr_matrix
from time import time

# Caracteristicas dos vertices
def vCaracteristicas(g):
    caracteristicasVerticesGrau = list()
    caracteristicasVerticesPageRank = list()

    #Indice,Grau Médio,Page Rank

    caracteristicasVerticesGrau = g.indegree(g.vs()) + g.outdegree(g.vs())
    caracteristicasVerticesPageRank = g.personalized_pagerank(g.vs())

    indicesGrau = [v.index for v in g.vs()]
    indicesPageRank = [v.index for v in g.vs()]

    caracteristicasVerticesGrau,indicesGrau = (list(x) for x in zip(*sorted(zip(caracteristicasVerticesGrau,indicesGrau), reverse = True)))
    caracteristicasVerticesPageRank,indicesPageRank = (list(x) for x in zip(*sorted(zip(caracteristicasVerticesPageRank,indicesPageRank), reverse = True)))

    return indicesGrau,indicesPageRank
# Montar subgrafo
def montarSubGrafo(g,verticesAtivos):
    g = Graph.subgraph(g,verticesAtivos)
    #g.es["label"] = g.es["weight"]
    g.simplify(combine_edges=dict(weight="sum"))
    return g
# Ler arquivo. Não é mais necessaria
def readSeed(Vetor,f):
    for line in f:
        Vetor = [line.rstrip() for line in open('InitialSeeds.txt')]
    return Vetor
# conversor Bool to string
def parseBoolString(string):
    value = bool
    if (string == "True" or string == "true"):
        value = True
    if (string == "False" or string == "false"):
        value = False
    return value
# Matriz W
def obterMatrizW(W,g,flag):
    if flag == 0:
        g.vs['s'] = g.strength(mode='all')
        for e in g.es:
            w_aux = e['weight']/g.vs[e.source]['s']
            W[e.source][e.target] = w_aux
        W = csr_matrix(W)
    if flag == 1:
        g.vs['s'] = g.strength(mode='in')
        for e in g.es:
            w_aux = e['weight']/g.vs[e.target]['s']
            W[e.source][e.target] = w_aux
        W = csr_matrix(W)
    if flag == 2:
        g.vs['s'] = g.strength(mode='out')
        for e in g.es:
            w_aux = e['weight']/g.vs[e.source]['s']
            W[e.source][e.target] = w_aux
        W = csr_matrix(W)
    return W
# obterSementesIniciais
def obterSementesIniciais(g,sementesIniciais,NUMVERT):
    b =  list()
    for v in g.vs:
        for j in sementesIniciais:
            if (j == v['name']):
                b.append(v.index)
    return b
# obterVetorEnergia
def obterVetorEnergia(g,sementesIniciais,NUMVERT):
    b =  np.zeros((NUMVERT),dtype = int)
    for v in g.vs:
        for j in sementesIniciais:
            if (j == v['name']):
                b[v.index] = 1
    return b
'''a = range(0,NUMVERT)
	for i in range(0,NUMVERT):
		if sementesIniciais.count(i) >= 1:
			a[i] = 1
		else:
			a[i] = 0
	return a'''
# Operação de Energia
def operacaoEnergia(g,verticesAtivos,vetorEnergia,espalhamentoGlobal,W,NUMVERT,limitePrecisao,limiteInferior):
    verticesAtivosOld = np.array([])
    vetorEnergiaOld = np.zeros((np.size(vetorEnergia)),dtype = np.float32)
    while((np.size(verticesAtivos) > np.size(verticesAtivosOld)) and ((np.fabs(vetorEnergia - vetorEnergiaOld)).any() > limiteInferior)):
        verticesAtivosOld = deepcopy(verticesAtivos)
        vetorEnergiaOld = np.array(vetorEnergia)
        vetorEnergia = ((1.0-espalhamentoGlobal)*(vetorEnergiaOld)) + (espalhamentoGlobal * (vetorEnergiaOld * W))
        for i in range(0,NUMVERT):
            if (vetorEnergia[i] > limitePrecisao and g.vs[i].index not in verticesAtivos):
                verticesAtivos.append(g.vs[i].index)
