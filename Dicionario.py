from Grafos import *

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

    digrafo.adicionarConexoes("A", "B", 4)
    digrafo.adicionarConexoes("A", "C", 1)
    digrafo.adicionarConexoes("B", "D", 7)
    digrafo.adicionarConexoes("C", "D", 3)

    digrafo.mostrarGrafo()


if __name__ == "__main__":
    main()
