from graph import Graph

class GraphBFS(Graph):
    def __init__(self, path=None, data=None):
        super().__init__(path, data)
    
    def search_bfs(self, v, get_colors=False):
        t = 0
        queue = list()
        entry_t = [0]*self._n
        parent = [0]*self._n
        node_lvl = [None]*self._n
        colors = list()
        for c in range(self._n):
            colors.append([None]*self._n)
        while 0 in entry_t:
            t += 1
            entry_t[v] = t
            node_lvl[v] = 0
            queue.append(v)
            while queue:
                v = queue.pop(0)
                for w in self.get_o_ngbhood(v):
                    if entry_t[w] == 0:
                        colors = self.color_edge(colors,v,w,"'0,0,255'")
                        parent[w] = v
                        node_lvl[w] = node_lvl[v]+1
                        t += 1
                        entry_t[w] = t
                        queue.append(w)
                    elif node_lvl[w] == node_lvl[v]:
                        if parent[w] == parent[v]:
                            colors = self.color_edge(colors,v,w,"'255,0,0'")
                        else:
                            colors = self.color_edge(colors,v,w,"'255,255,0'")
                    elif node_lvl[w] == node_lvl[v]+1:
                        colors = self.color_edge(colors,v,w,"'0,255,0'")
        if get_colors:
            return colors
        return node_lvl
    
    def color_edge(self, m, v, w, color):
        if v < w:
            m[v][w] = color
        else:
            m[w][v] = color
        return m