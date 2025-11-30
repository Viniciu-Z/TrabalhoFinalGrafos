from Grafos import *
from DicionarioGrafo import *
from DicionarioDigrafo import *

def main():
    grafo = Grafo(ponderado=True)

    grafo.adicionarConexoes('A', 'B', 11)
    grafo.adicionarConexoes('A', 'C', 18)
    grafo.adicionarConexoes('A', 'D', 20)
    grafo.adicionarConexoes('A', 'F', 12)
    grafo.adicionarConexoes('B', 'C', 9)
    grafo.adicionarConexoes('B', 'D', 8)
    grafo.adicionarConexoes('B', 'E', 7.5)
    grafo.adicionarConexoes('C', 'D', 7)
    grafo.adicionarConexoes('C', 'F', 8.5)
    grafo.adicionarConexoes('D', 'E', 10)
    grafo.adicionarConexoes('E', 'F', 5)

    #grafo.mostrarGrafo()
    '''
    print(f"quantidade de vertices no grafo {verticesNoGrafo(grafo)}")
    print(f"quantidade de arestas no grafo {arestasNoGrafo(grafo)}")
    print(f"D: {vizinhancaGrafo(grafo,"D")}")
    print(f"grau de D: {grauGrafo(grafo, 'D')}")
    print(f"Peso da aresta B - D: {pesoArestaGrafo(grafo, 'B', 'D')}")
    print(f"Vertice com o maior grau: {maiorGrauGrafo(grafo)}")
    print(f"Vertice como menor grau: {menorGrauGrafo(grafo)}")
    
    ordem, distancias, filas = bfsGrafo(grafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    '''
    ordem, inicio, fim = dfsGrafo(grafo, "A")
    print(f"Ordem de visita: {ordem}")
    print(f"inicio: {inicio}")
    print(f"fim: {fim}")
    '''
    distancias, visitados = bellmanfordGrafo(grafo, "A")
    print(f"distancias: {distancias}")
    print(f"visitados: {visitados}")
    

    distancias, predecesor = dijkstraGrafo(grafo, "A")
    print(distancias)
    print(predecesor)
    '''

#{'A': 0, 'B': 11, 'C': 18, 'D': 19, 'F': 12, 'E': 17}
#{'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'F': 'A', 'E': 'F'}

if __name__ == "__main__":
    main()
