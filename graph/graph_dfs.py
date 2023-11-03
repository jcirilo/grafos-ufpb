from graph.graph import Graph

class GraphDFS(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
        self.t = 0

    def search_dfs(self, v):
        self.t = 0
        pe = [0]*self._n
        ps = [0]*self._n
        parent = [None]*self._n
        colors = list()
        for c in range(self._n):
            colors.append([None]*self._n)
        self.__depth_search__(v, pe, ps, parent, colors)
        return colors
    
    def __depth_search__(self, v, pe, ps, parent, colors):
        self.t += 1
        pe[v] = self.t
        for w in self.get_o_ngbhood(v):
            if pe[w] == 0:
                colors = self.color_edge(colors,v,w,"'0,0,255'")
                parent[w] = v
                self.__depth_search__(w, pe, ps, parent, colors)
            elif ps[w] == 0 and w != parent[v]:
                colors = self.color_edge(colors,v,w,"'255,0,0'")
        self.t += 1
        ps[v] = self.t
    
    def color_edge(self, m, v, w, color):
        if v < w:
            m[v][w] = color
        else:
            m[w][v] = color
        return m