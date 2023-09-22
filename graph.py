from re import finditer 

# grafo com busca em largura e profundidade (bfs e dfs)
class Graph:
    def __init__(self, path=None, data=None):
        self.n = 0
        self.adj_matrix = list()
        self.adj_list = list()
        self.t = 0
        if path:
            self.load_file(path)
        elif data:
            self.load_data(data)

    def load_data(self, data):
        self.n = len(data[0])
        self.adj_matrix = data
        for i in range(self.n):
            self.adj_list.append(list())
            for j in range(self.n):
                if self.adj_matrix[i][j]:
                    self.adj_list[i].append(j)

    def load_file(self, path):
        file_iter = open(path, 'r')
        self.n = int(next(file_iter))
        for i in range(self.n):
            self.adj_list.append(list())
            self.adj_matrix.append(list())
            int_iter = finditer('[\d]', next(file_iter))
            for j in range(self.n):
                is_adj = int(next(int_iter).group())
                self.adj_matrix[i].append(is_adj)
                if is_adj:
                    self.adj_list[i].append(j)
        file_iter.close()

    def degree(self, v):
        return len(self.adj_list[v])

    def dmax(self):
        max = self.degree(0)
        for i in range(1, self.n):
            aux = self.degree(i)
            if aux >= max:
                max = aux
        return max

    def dmin(self):
        min = self.degree(0)
        for i in range(1, self.n):
            aux = self.degree(i)
            if aux <= min:
                min = aux
        return min

    def degrees(self):
        l = list()
        for i in range(self.n):
            l.append(self.degree(i))
        return sorted(l)

    def opn_ngbhood(self, v):
        return self.adj_list[v]

    def cls_ngbhood(self, v):
        aux = self.adj_list[v]
        aux.insert(v, v)
        return aux

    def is_adj(self, a, b):
        if a | b > self.n:
            return False
        return self.adj_matrix[a][b] == 1

    def regularity(self):
        first_degree = self.degree(0)
        for i in range(1, self.n):
            if first_degree != self.degree(i):
                return -1
        return first_degree

    def is_complete(self):
        max_edges = (self.n*(self.n-1)/2)
        current_edges = 0
        for i in range(1, self.n):
            current_edges += self.degree(i)
        current_edges /= 2
        return current_edges == max_edges

    def universal_nodes(self):
        out = list()
        for i in range(self.n):
            if self.degree(i) == self.n-1:
                out.append(i)
        return out
    
    def isolated_nodes(self):
        out = list()
        for i in range(self.n):
            if self.degree(i) == 0:
                out.append(i)
        return out
    
    def is_sub(self, n, m):
        if len(n) > self.n:
            return False
        for i in n:
            if i > self.n:
                return False
        for v in m:
            if v[0] | v[1] > self.n:
                return False
            if not self.is_adj(v[0], v[1]):
                return False
        return True

    def is_ride(self, n):
        for i in range(self.n):
            if not self.is_adj(n[i], n[i+1]):
                return False
        return True
    
    def is_way(self, n):
        if not self.is_ride(n):
            return False
        for i in range(self.n-1):
            for j in range(i, self.n):
                if n[i] == n[j]:
                    return False
        return True
    
    def is_cicle(self, n):
        if n[0] != n[len(n)-1]:
            return False
        if not self.is_ride(n):
            return False
        for i in range(self.n-1):
            for j in range(i+1, self.n-1):
                if n[k] == n[j]:
                    return False
        return True

    def is_clique(self, n):
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                if self.is_adj(n[i], n[j]):
                    return False
        return True
    
    def complement(self, g):
        data = list()
        for i in range(self.n):
            data.append(list())
            for j in range(self.n): 
                data[i].append(0 if j == i else 1-g.adj_matrix[i][j])
        return Graph(data=data)

    def is_independent(self, n):
        return self.complement().g.is_cicle(n)

    def dist(self, v, w):
        node_lvl = self.search_bfs(v)
        return node_lvl[w]

    def node_eccentricity(self, v):
        node_lvl = self.search_bfs(v)
        eccentricity = max(node_lvl)
        return eccentricity
    
    def eccentricity_list(self):
        e_list = list()
        for v in range(self.n):
            e_list.append(self.node_eccentricity(v))
        return e_list

    def radius(self):
        return min(self.eccentricity_list())
    
    def diameter(self):
        return max(self.eccentricity_list())

    def apl(self): #average path length
        sum1 = 0
        sum2 = 0
        for v in range(self.n):
            for lvl in self.search_bfs(v):
                sum1 += lvl
            sum1 /= self.n-1
            sum2 += sum1
            sum1 = 0
        return sum2/self.n

    def search_bfs(self, v, get_colors=False):
        t = 0
        queue = list()
        entry_t = [0]*self.n
        parent = [0]*self.n
        node_lvl = [None]*self.n
        colors = list()
        for c in range(self.n):
            colors.append([None]*self.n)
        while 0 in entry_t:
            t += 1
            entry_t[v] = t
            node_lvl[v] = 0
            queue.append(v)
            while queue:
                v = queue.pop(0)
                for w in self.opn_ngbhood(v):
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

    def search_dfs(self, v):
        self.t = 0
        pe = [0]*self.n
        ps = [0]*self.n
        parent = [None]*self.n
        colors = list()
        for c in range(self.n):
            colors.append([None]*self.n)
        self.__depth_search__(v, pe, ps, parent, colors)
        return colors
    
    def __depth_search__(self, v, pe, ps, parent, colors):
        self.t += 1
        pe[v] = self.t
        for w in self.opn_ngbhood(v):
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