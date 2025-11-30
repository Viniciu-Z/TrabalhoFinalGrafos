from Grafos import *
from DicionarioDigrafo import *

def main():
    digrafo = Digrafo.Grafo(ponderado=True)

    digrafo.adicionarConexoes('A', 'B', 11) #A->B
    digrafo.adicionarConexoes('A', 'C', 18) #A->C
    digrafo.adicionarConexoes('A', 'D', 20) #A->D
    digrafo.adicionarConexoes('F', 'A', 12) #F->A
    digrafo.adicionarConexoes('B', 'C', 9)  #B->C
    digrafo.adicionarConexoes('B', 'D', 8)  #B->D
    digrafo.adicionarConexoes('B', 'E', 7.5)#B->E
    digrafo.adicionarConexoes('C', 'D', 7)  #C->D
    digrafo.adicionarConexoes('F', 'C', 8.5)#F->C
    digrafo.adicionarConexoes('D', 'E', 10) #D->E
    digrafo.adicionarConexoes('E', 'F', 5)  #E->F

    digrafo.mostrarGrafo()
    '''
    print(f"quantidade de vertices no grafo {verticesNoDigrafo(digrafo)}")
    print(f"quantidade de arestas no grafo {arestasNoDigrafo(digrafo)}")
    print(f"D: {vizinhancaDigrafo(digrafo, "D")}")
    print(f"grau de D: {grauDigrafo(digrafo, 'D')}")
    print(f"Peso da aresta B -> D: {pesoArestaDigrafo(digrafo, 'B', 'D')}")
    print(f"Vertice com maior grau: {maiorGrauDigrafo(digrafo)}")
    print(f"Vertice com o menor grau: {menorGrauDigrafo(digrafo)}")

    distancias, ordem = bfsDigrafo(digrafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    
    ordem, inicio, fim = dfsDigrafo(digrafo, "A")
    print(f"ordem: {ordem}")
    print(f"inicio: {inicio}")
    print(f"fim: {fim}")

    ordem, distancias = bellmanfordDigrafo(digrafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    
    distancias, ordem = dijkstraDigrafo(digrafo, "A")
    print(f"ordem: {ordem}")
    print(f"distancias: {distancias}")
    '''

    print(coloracaoDigrafo(digrafo))


if __name__ == "__main__":
    main()
