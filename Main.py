from Grafos import *
from Dicionario import *

grafo = Grafo(ponderado=True)

grafo.adicionarConexoes("A", "B", 3)
grafo.adicionarConexoes("A", "C", 2)
grafo.adicionarConexoes("B", "D", 5)
grafo.adicionarConexoes("C", "D", 1)
grafo.adicionarConexoes("D", "E", 2)
grafo.adicionarConexoes("E", "A", 3)

grafo.mostrarGrafo()

print(f"quantidade de vertices no grafo {verticesNoGrafo(grafo)}")
print(f"quantidade de arestas no grafo {arestasNoGrafo(grafo)}")
