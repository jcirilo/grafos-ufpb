from graph import Graph
from edge import ColoredEdge

# Grafo com busca em profundidade
class DepthGraph(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
        self.t = 0
        self.pe = list()
        self.ps = list()
        self.parent = list()
        self.edges = list()
        for i in range(self.n):
            self.pe.append(0)
            self.ps.append(0)
            self.parent.append(None)
            self.edges.append(list())

    def depth_search(self, v):
        self.t = 0
        for i in range(self.n):
            self.pe[i] = 0
            self.ps[i] = 0
            self.parent[i] = None
            self.edges[i].clear()
        self.p(v)
        self.write_out_file()

    def p(self, v):
        self.t += 1
        self.pe[v] = self.t
        for w in self.get_open_neighbourhood(v):
            if self.pe[w] == 0:
                self.parent[w] = v
                self.add_colored_edge(v,w,'0,0,255')
                self.p(w)
            elif self.ps[w] == 0 and w != self.parent[v]:
                self.add_colored_edge(v,w,'255,0,0')
        self.t += 1
        self.ps[v] = self.t

    def add_colored_edge(self, v, w, color):
        if v < w:
            self.edges[v].append(ColoredEdge(w, color))
        else:
            self.edges[w].append(ColoredEdge(v, color))

    def write_out_file(self):
        for i in range(self.n):
            for e in self.edges[i]:
                print("{},{},false,'{}'".format(i+1, e.to_vertex+1, e.color))

g = DepthGraph('in/graph_2')
g.depth_search(0)