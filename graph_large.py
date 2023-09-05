from graph import Graph

class LargeGraph(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
        self.queue = list()
        self.t = 0
        self.l = list()
        self.parent = list()
        self.node_level = list()
        self.color_palette = ['0,0,0', '0,0,255', '255,0,0', '0,255,0', '255,255,0']
        self.colored_edges = list()
        for i in range(self.n):
            self.l.append(0)
            self.node_level.append(0)
            self.parent.append(None)
            self.colored_edges.append(list())

    def large_search(self, v):
        self.t = 0
        self.queue.clear()
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i].append(0)
        for i in range(self.n):
            self.parent[i] = None
            self.l[i] = 0
        while 0 in self.l:
            self.t += 1
            self.l[v] = self.t
            self.node_level[v] = 0
            self.queue.append(v)
            self.search()
        return self.colored_edges

    def search(self):
        while len(self.queue) != 0:
            v = self.queue.pop(0)
            for w in self.opn_ngbhood(v):
                if self.l[w] == 0:
                    self.color_edge(v,w,1)
                    self.parent[w] = v
                    self.node_level[w] = self.node_level[v]+1
                    self.t += 1
                    self.l[w] = self.t
                    self.queue.append(w)
                elif self.node_level[w] == self.node_level[v]:
                    if self.parent[w] == self.parent[v]:
                        self.color_edge(v,w,2)
                    else:
                        self.color_edge(v,w,4)
                elif self.node_level[w] == self.node_level[v]+1:
                        self.color_edge(v,w,3)

    def color_edge(self, v, w, color):
        if v < w:
            self.colored_edges[v][w] = color
        else:
            self.colored_edges[w][v] = color