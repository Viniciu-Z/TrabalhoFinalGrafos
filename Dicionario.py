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


