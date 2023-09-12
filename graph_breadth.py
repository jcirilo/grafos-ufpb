from graph import Graph

class GraphBreadth(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
        self.t = 0
        self.queue = list()
        self.entry_time = list()
        self.parent = list()
        self.node_level = list()
        self.colored_edges = list()
        for i in range(self.n):
            self.entry_time.append(0)
            self.parent.append(None)
            self.node_level.append(0)
            self.colored_edges.append(list())
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i].append(0)

    def search(self, v):
        self.t = 0
        self.queue.clear()
        for i in range(self.n):
            self.parent[i] = None
            for j in range(self.n):
                self.colored_edges[i][j] = 0
        while 0 in self.entry_time:
            self.t += 1
            self.entry_time[v] = self.t
            self.node_level[v] = 0
            self.queue.append(v)
            self.__breadth_search__()
        return self.colored_edges

    def __breadth_search__(self):
        while len(self.queue) != 0:
            v = self.queue.pop(0)
            for w in self.opn_ngbhood(v):
                if self.entry_time[w] == 0:
                    self.color_edge(v,w,1)
                    self.parent[w] = v
                    self.node_level[w] = self.node_level[v]+1
                    self.t += 1
                    self.entry_time[w] = self.t
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