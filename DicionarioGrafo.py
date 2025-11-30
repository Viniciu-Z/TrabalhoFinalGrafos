import heapq
from collections import deque
from collections import defaultdict
from Grafos import Grafo

def verticesNoGrafo(grafo):
    return len(grafo.vertices)

def arestasNoGrafo(grafo):
    arestas = set()
    for vertice in grafo.vertices:
        for vizinho, peso in grafo.vertices[vertice]:
            aresta = tuple(sorted((vertice, vizinho)))
            arestas.add(aresta)
    return len(arestas)

def vizinhancaGrafo(grafo, inicio):
    return grafo.vertices[inicio]

def grauGrafo(grafo, inicio):
    return len(grafo.vertices[inicio])

def pesoArestaGrafo(grafo, verticeInicial, verticeFinal):
    for destino, peso in grafo.vertices[verticeInicial]:
        if destino == verticeFinal:
            return peso
    return None

def maiorGrauGrafo(grafo):
    maior = 0
    verticeMaiorGrau = None

    for vertice in grafo.vertices:
        grau = grauGrafo(grafo, vertice)

        if grau > maior:
            maior = grau
            verticeMaiorGrau = vertice

    return (verticeMaiorGrau, maior)

def menorGrauGrafo(grafo):
    menor = 100
    verticeMenorGrau = None

    for vertice in grafo.vertices:
        grau = grauGrafo(grafo, vertice)

        if grau < menor:
            menor = grau
            verticeMenorGrau = vertice

    return (verticeMenorGrau, menor)

def bfsGrafo(grafo, inicio):
    visitados = []
    fila = deque(inicio)
    distancias = {inicio: 0}
    ordem = {}

    while fila:
        vertice = fila.popleft()

        if vertice not in visitados:
            visitados.append(vertice)

            for vizinho, peso in grafo.vertices[vertice]:
                if vizinho not in visitados and vizinho not in fila:
                    distancias[vizinho] = distancias[vertice] + peso
                    ordem[vizinho] = vertice
                    fila.append(vizinho)
    return ordem, distancias

def dfsGrafo(grafo, verticeInicial):
    tempo = 0
    visitados = []
    inicio = {}
    fim = {}

    ordem = {}
    for vertice in grafo.vertices:
        ordem[vertice] = None

    def dfsVisita(vertice):
        nonlocal tempo
        visitados.append(vertice)

        tempo += 1
        inicio[vertice] = tempo

        for vizinho, peso in grafo.vertices[vertice]:
            if vizinho not in visitados:
                ordem[vizinho] = vertice
                dfsVisita(vizinho)

        tempo += 1
        fim[vertice] = tempo

    dfsVisita(verticeInicial)
    return ordem, inicio, fim

def bellmanfordGrafo(grafo, inicio):
    distancias = {}
    ordem = {}

    for vertice in grafo.vertices:
        distancias[vertice] = float('inf')
        ordem[vertice] = None

    distancias[inicio] = 0

    for _ in range(len(grafo.vertices) - 1):
        for vertice in grafo.vertices:
            for vizinho, peso in grafo.vertices[vertice]:
                if distancias[vertice] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[vertice] + peso
                    ordem[vizinho] = vertice

    for vertice in grafo.vertices:
        for vizinho, peso in grafo.vertices[vertice]:
            if distancias[vertice] + peso < distancias[vizinho]:
                print("Ciclo negativo")
                return None, None

    return ordem, distancias

def dijkstraGrafo(grafo, inicio):
    heap = [(0, inicio)]
    distancias = {}
    ordem = {}
    visitados = []

    for vertice in grafo.vertices:
        distancias[vertice] = float('inf')
        ordem[vertice] = None
    distancias[inicio] = 0

    while heap:
        distancia, vertice = heapq.heappop(heap)

        if vertice not in visitados:
            for vizinho, peso in grafo.vertices[vertice]:
                novaDistancia = distancia + peso
                if novaDistancia < distancias[vizinho]:
                    distancias[vizinho] = novaDistancia
                    ordem[vizinho] = vertice
                    heapq.heappush(heap, (novaDistancia, vizinho))

    return distancias, ordem









