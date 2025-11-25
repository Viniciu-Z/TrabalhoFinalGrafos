from Grafos import *
from DicionarioGrafo import *
from DicionarioDigrafo import *

def main():
    grafo = Grafo(ponderado=True)

    grafo.adicionarConexoes("A", "B", 3)
    grafo.adicionarConexoes("A", "C", 2)
    grafo.adicionarConexoes("B", "D", 5)
    grafo.adicionarConexoes("C", "D", 1)
    grafo.adicionarConexoes("D", "E", 2)

    grafo.mostrarGrafo()
    '''
    print(f"quantidade de vertices no grafo {verticesNoGrafo(grafo)}")
    print(f"quantidade de arestas no grafo {arestasNoGrafo(grafo)}")
    print(f"D: {vizinhancaGrafo(grafo,"D")}")
    print(f"grau de D: {grauGrafo(grafo, 'D')}")
    print(f"Peso da aresta B - D: {pesoArestaGrafo(grafo, 'B', 'D')}")
    print(f"Vertice com o maior grau: {maiorGrauGrafo(grafo)}")
    print(f"Vertice como menor grau: {menorGrauGrafo(grafo)}")
    '''
    ordem, distancias, filas = bfsGrafo(grafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    print(f"filas: {filas}")

if __name__ == "__main__":
    main()
