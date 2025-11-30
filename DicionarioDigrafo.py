from Grafos import Digrafo
import heapq
import random
from collections import deque, defaultdict


def verticesNoDigrafo(digrafo):
    return len(digrafo.vertices)

def arestasNoDigrafo(digrafo):
    arestas = set()
    for vertice in digrafo.vertices:
        for vizinho, peso in digrafo.vertices[vertice]:
            aresta = tuple(sorted((vertice, vizinho)))
            arestas.add(aresta)
    return len(arestas)

def vizinhancaDigrafo(digrafo, vertice):
    vizinhos = []

    for chegando in digrafo.vertices:
        for destino, peso in digrafo.vertices[chegando]:
            if destino == vertice and chegando not in vizinhos:
                vizinhos.append((chegando, peso))

    for destino, peso in digrafo.vertices[vertice]:
        if destino not in vizinhos:
            vizinhos.append((destino, peso))

    return vizinhos

def grauDigrafo(grafo, vertice):
    grau = len(grafo.vertices[vertice])

    for chegando in grafo.vertices:
        for vizinho, peso in grafo.vertices[chegando]:
            if vizinho == vertice:
                grau += 1
    return grau

def pesoArestaDigrafo(digrafo, verticeInicial, verticeFinal):
    for destino, peso in digrafo.vertices[verticeInicial]:
        if destino == verticeFinal:
            return peso
    return None

def maiorGrauDigrafo(digrafo):
    maior = 0
    verticeMaiorGrau = None

    for vertice in digrafo.vertices:
        grau = grauDigrafo(digrafo, vertice)
        if grau > maior:
            maior = grau
            verticeMaiorGrau = vertice

    return (verticeMaiorGrau, maior)

def menorGrauDigrafo(digrafo):
    menor = 100
    verticeMenorGrau = None

    for vertice in digrafo.vertices:
        grau = grauDigrafo(digrafo, vertice)
        if grau < menor:
            menor = grau
            verticeMenorGrau = vertice

    return (verticeMenorGrau, menor)

def bfsDigrafo(digrafo, inicio):
    visitados = []
    fila = deque(inicio)
    distancia = {inicio: 0}
    ordem = {}

    while fila:
        inicio = fila.popleft()
        if inicio not in visitados:
            visitados.append(inicio)

            for vizinho, peso in digrafo.vertices[inicio]:
                if vizinho not in visitados and vizinho not in fila:
                    distancia[vizinho] = distancia[inicio] + peso
                    ordem[vizinho] = inicio
                    fila.append(vizinho)
    return distancia, ordem

def dfsDigrafo(digrafo, verticeInicial):
    tempo = 0
    visitados = []
    inicio = {}
    fim = {}

    ordem = {}
    for vertice in digrafo.vertices:
        ordem[vertice] = None

    def dfsVisita(vertice):
        nonlocal tempo
        visitados.append(vertice)

        tempo += 1
        inicio[vertice] = tempo

        for vizinho, peso in digrafo.vertices[vertice]:
            if vizinho not in visitados:
                ordem[vizinho] = vertice
                dfsVisita(vizinho)

        tempo += 1
        fim[vertice] = tempo

    dfsVisita(verticeInicial)
    return ordem, inicio, fim

def bellmanfordDigrafo(digrafo, inicio):
    distancias = {}
    ordem = {}

    for vertice in digrafo.vertices:
        distancias[vertice] = float('inf')
        ordem[vertice] = None

    distancias[inicio] = 0

    for _ in range(len(digrafo.vertices) - 1):
        for vertice in digrafo.vertices:
            for vizinho, peso in digrafo.vertices[vertice]:
                if distancias[vertice] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[vertice] + peso
                    ordem[vizinho] = vertice

    for vertice in digrafo.vertices:
        for vizinho, peso in digrafo.vertices[vertice]:
            if distancias[vertice] + peso < distancias[vizinho]:
                print("Ciclo negativo")
                return None, None

    return ordem, distancias

import heapq

def dijkstraDigrafo(digrafo, inicio):
    heap = [(0, inicio)]
    distancias = {}
    ordem = {}
    visitados = set()

    for vertice in digrafo.vertices:
        distancias[vertice] = float('inf')
        ordem[vertice] = None
    distancias[inicio] = 0

    while heap:
        distancia, vertice = heapq.heappop(heap)

        if vertice in visitados:
            continue
        visitados.add(vertice)

        for vizinho, peso in digrafo.vertices[vertice]:
            novaDistancia = distancia + peso
            if novaDistancia < distancias[vizinho]:
                distancias[vizinho] = novaDistancia
                ordem[vizinho] = vertice
                heapq.heappush(heap, (novaDistancia, vizinho))

    return distancias, ordem

def coloracaoDigrafo(digrafo):
    cores = {}
    for vertice in digrafo.vertices:
        cores[vertice] = None

    for vertice in digrafo.vertices:
        coresUsadas = []

        for vizinho, peso in digrafo.vertices[vertice]:
            if cores[vizinho] is not None:
                coresUsadas.append(cores[vizinho])

        for vizinho in digrafo.vertices:
            for destino, peso in digrafo.vertices[vizinho]:
                if destino == vertice and cores[vizinho] is not None:
                    coresUsadas.append(cores[vizinho])

        cor = 1
        while cor in coresUsadas:
            cor += 1
        cores[vertice] = cor

    return cores
