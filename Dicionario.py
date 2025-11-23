import Grafos
from Grafos import *

def verticesNoGrafo(grafo):
    vertices = []
    for vertice in grafo.vertices:
        vertices.append(vertice)
    return len(vertices)

def arestasNoGrafo(grafo):
    arestas = set()
    for vertice in grafo.vertices:
        for vizinho, peso in grafo.vertices[vertice]:
            aresta = tuple(sorted((vertice, vizinho)))
            arestas.add(aresta)
    return len(arestas)

def vizinhanca(grafo, vertice):
    vizinhos = []
    for destino, peso in grafo.vertices[vertice]: #destino são os vertices InNeighbor
        if destino not in vizinhos:
            vizinhos.append(destino)

    for chegando in grafo.vertices: #chegando são os vertices OutNeighbor
        for destino, peso in grafo.vertices[chegando]:
            if destino == vertice and chegando not in vizinhos:
                vizinhos.append(chegando)
    return vizinhos

def graus(grafo, vertice):
    grau = len(grafo.vertices[vertice])

    if isinstance(grafo, Digrafo.Grafo):
        for chegando in grafo.vertices:
            for vizinho, peso in grafo.vertices[chegando]:
                if vizinho == vertice:
                    grau += 1
    return grau

def pesoDaAresta(grafo, vertice, vizinho):
    for destino, peso in grafo.vertices[vertice]:
        if destino == vizinho:
            return peso
    return None

def maiorGrau(grafo):
    maior = 0
    for vertice in grafo.vertices:
        grau = graus(grafo, vertice)
        if grau > maior:
            maior = grau
    return maior

def menorGrau(grafo):
    menor = 100
    for vertice in grafo.vertices:
        grau = graus(grafo, vertice)
        if grau < menor:
            menor = grau
    return menor
