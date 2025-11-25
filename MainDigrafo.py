from Grafos import *
from DicionarioDigrafo import *

def main():
    digrafo = Digrafo.Grafo(ponderado=True)

    digrafo.adicionarConexoes("A", "B", 4)  # A -> B
    digrafo.adicionarConexoes("A", "C", 1)  # A -> C
    digrafo.adicionarConexoes("B", "D", 7)  # B -> D
    digrafo.adicionarConexoes("C", "D", 3)  # C -> D
    digrafo.adicionarConexoes("D", "E", 1)  # D -> E

    digrafo.mostrarGrafo()
    '''
    print(f"quantidade de vertices no grafo {verticesNoDigrafo(digrafo)}")
    print(f"quantidade de arestas no grafo {arestasNoDigrafo(digrafo)}")
    print(f"D: {vizinhancaDigrafo(digrafo, "D")}")
    print(f"grau de D: {grauDigrafo(digrafo, 'D')}")
    print(f"Peso da aresta B -> D: {pesoArestaDigrafo(digrafo, 'B', 'D')}")
    print(f"Vertice com maior grau: {maiorGrauDigrafo(digrafo)}")
    print(f"Vertice com o menor grau: {menorGrauDigrafo(digrafo)}")
    '''
    ordem, distancias, filas = bfsDigrafo(digrafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    print(f"filas: {filas}")

if __name__ == "__main__":
    main()
