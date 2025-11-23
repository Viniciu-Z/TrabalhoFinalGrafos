from Grafos import *
from Dicionario import *

def main():
    print("=== Grafo Não Direcionado ===")
    grafo = Grafo(ponderado=True)

    grafo.adicionarConexoes("A", "B", 3)
    grafo.adicionarConexoes("A", "C", 2)
    grafo.adicionarConexoes("B", "D", 5)
    grafo.adicionarConexoes("C", "D", 1)

    grafo.mostrarGrafo()

    print("\n=== Digrafo (Direcionado) ===")
    digrafo = Digrafo.Grafo(ponderado=True)

    digrafo.adicionarConexoes("A", "B", 4)  # A -> B
    digrafo.adicionarConexoes("A", "C", 1)  # A -> C
    digrafo.adicionarConexoes("B", "D", 7)  # B -> D
    digrafo.adicionarConexoes("C", "D", 3)  # C -> D
    digrafo.adicionarConexoes("D", "E", 1)  # D -> E

    digrafo.mostrarGrafo()

    # print(f"quantidade de vertices no grafo {verticesNoGrafo(grafo)}")
    # print(f"quantidade de arestas no grafo {arestasNoGrafo(grafo)}")
    # print(vizinhanca(digrafo, "E"))
    # print(graus(digrafo, "D"))
    # print(pesoDaAresta(digrafo,"A","B"))
    # print(maiorGrau(digrafo))
    # print(menorGrau(digrafo))


if __name__ == "__main__":
    main()
