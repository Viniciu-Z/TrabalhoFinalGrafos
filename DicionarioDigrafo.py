from collections import deque
from Grafos import Digrafo

def verticesNoDigrafo(digrafo):
    return len(digrafo.vertices)

def arestasNoDigrafo(grafo):
    arestas = set()
    for vertice in grafo.vertices:
        for vizinho, peso in grafo.vertices[vertice]:
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

def pesoArestaDigrafo(digrafo, vertice, vizinho):
    for destino, peso in digrafo.vertices[vertice]:
        if destino == vizinho:
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

def bfsDigrafo(digrafo, vertice):
    visitados = []
    fila = deque(vertice)
    ordemDaVisita = []
    distancia = {vertice: 0}
    predecesor = {}

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.append(vertice)
            ordemDaVisita.append(vertice)
            for vizinho, peso in digrafo.vertices[vertice]:
                if vizinho not in visitados and vizinho not in fila:
                    distancia[vizinho] = distancia[vertice] + peso
                    predecesor[vizinho] = vertice
                    fila.append(vizinho)
    return ordemDaVisita, distancia, predecesor