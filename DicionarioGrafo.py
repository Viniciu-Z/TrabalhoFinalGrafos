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

def vizinhancaGrafo(grafo, vertice):
    return grafo.vertices[vertice]

def grauGrafo(grafo, vertice):
    return len(grafo.vertices[vertice])

def pesoArestaGrafo(grafo, vertice, vizinho):
    for destino, peso in grafo.vertices[vertice]:
        if destino == vizinho:
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