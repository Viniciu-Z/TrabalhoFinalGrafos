class Grafo:
    def __init__(self, ponderado=False):
        self.vertices = {}
        self.ponderado = ponderado

    def adicionarConexoes(self, vertice, vizinho, peso=1):
        if not self.ponderado:
            peso = 1

        if vertice not in self.vertices:
            self.vertices[vertice] = []
        if vizinho not in self.vertices:
            self.vertices[vizinho] = []

        self.vertices[vertice].append((vizinho, peso))
        self.vertices[vizinho].append((vertice, peso))

    def mostrarGrafo(self):
        for vertice in self.vertices:
            print(f"{vertice}: {self.vertices[vertice]}")

class Digrafo:
    class Grafo:
        def __init__(self, ponderado=False):
            self.vertices = {}
            self.ponderado = ponderado

        def adicionarConexoes(self, vertice, vizinho, peso=1):
            if not self.ponderado:
                peso = 1

            if vertice not in self.vertices:
                self.vertices[vertice] = []
            if vizinho not in self.vertices:
                self.vertices[vizinho] = []

            self.vertices[vertice].append((vizinho, peso))

        def mostrarGrafo(self):
            for vertice in self.vertices:
                print(f"{vertice}: {self.vertices[vertice]}")
