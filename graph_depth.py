from graph import Graph
from os.path import join

# Grafo com busca em profundidade
class GraphDepth(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
        self.t = 0
        self.pe = list()
        self.ps = list()
        self.parent = list()
        self.color_palette = ['0,0,0', '0,0,255', '255,0,0', '0,255,0', '255,255,0']
        self.colored_edges = list()
        for i in range(self.n):
            self.pe.append(0)
            self.ps.append(0)
            self.parent.append(None)
            self.colored_edges.append(list())
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i].append(0)

    def search(self, v):
        self.t = 0
        for i in range(self.n):
            self.pe[i] = 0
            self.ps[i] = 0
            self.parent[i] = None
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i][j] = 0
        self.__depth_search__(v)
        return self.colored_edges

    def __depth_search__(self, v):
        self.t += 1
        self.pe[v] = self.t
        for w in self.opn_ngbhood(v):
            if self.pe[w] == 0:
                self.color_edge(v,w, 1)
                self.parent[w] = v
                self.__depth_search__(w)
            elif self.ps[w] == 0 and w != self.parent[v]:
                self.color_edge(v,w, 2)
        self.t += 1
        self.ps[v] = self.t

    def color_edge(self, v, w, color):
        if v < w:
            self.colored_edges[v][w] = color
        else:
            self.colored_edges[w][v] = color