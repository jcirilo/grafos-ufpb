from re import finditer 

# grafo com busca em largura e profundidade (bfs e dfs)
class Graph:
    def __init__(self, path=None, data=None):
        # grafo
        self.n = 0
        self.adj_matrix = list()
        self.adj_list = list()
        # buscas
        self.t = 0                  # bfs/dfs
        self.in_t = list()          # bfs/dfs
        self.out_t = list()         # dfs
        self.parent = list()        # bfs/dfs
        self.colored_edges = list() # bfs/dfs
        self.node_lvl = list()      # bfs
        # ler e carrega os dados do grafo
        if path:
            self.load_file(path)
        elif data:
            self.load_data(data)
        # inicializa as listas de busca
        for i in range(self.n):
            self.in_t.append(0)
            self.out_t.append(0)
            self.parent.append(None)
            self.node_lvl.append(None)
            self.colored_edges.append(list())
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i].append(0)

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
        sorted = []
        for i in range(self.n):
            sorted.append(self.degree(i))
        sorted.sort()
        return sorted

    def opn_ngbhood(self, v):
        return self.adj_list[v]

    def cls_ngbhood(self, v):
        aux = self.adj_list[v]
        aux.append(v)
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

    def node_eccentricity(self, v):
        self.breadth_search(v, only_lvl=True)
        eccentricity = max(self.node_lvl)
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

    def depth_search(self, v):
        self.t = 0
        for i in range(self.n):
            self.in_t[i] = 0
            self.out_t[i] = 0
            self.parent[i] = None
        for i in range(self.n):
            for j in range(self.n):
                self.colored_edges[i][j] = 0
        self.__depth_search__(v)
        return self.colored_edges

    def breadth_search(self, v, only_lvl=False):
        self.t = 0
        queue = list()
        if not only_lvl:
            for i in range(self.n):
                for j in range(self.n):
                    self.colored_edges[i][j] = 0
        for i in range(self.n):
            self.in_t[i] = 0
            self.parent[i] = 0
            self.node_lvl[i] = None
        while 0 in self.in_t:
            self.t += 1
            self.in_t[v] = self.t
            self.node_lvl[v] = 0
            queue.append(v)
            self.__breadth_search__(queue, only_lvl)
        return self.colored_edges

    def __breadth_search__(self, queue, only_lvl):
        while queue:
            v = queue.pop(0)
            for w in self.opn_ngbhood(v):
                if self.in_t[w] == 0:
                    if not only_lvl: self.__color_edge__(v,w, color_code=1)
                    self.parent[w] = v
                    self.node_lvl[w] = self.node_lvl[v]+1
                    self.t += 1
                    self.in_t[w] = self.t
                    queue.append(w)
                elif not only_lvl and self.node_lvl[w] == self.node_lvl[v]:
                    if self.parent[w] == self.parent[v]:
                        self.__color_edge__(v,w, color_code=2)
                    else:
                        self.__color_edge__(v,w, color_code=3)
                elif not only_lvl and self.node_lvl[w] == self.node_lvl[v]+1:
                    self.__color_edge__(v,w, color_code=4)

    def __depth_search__(self, v):
        self.t += 1
        self.in_t[v] = self.t
        for w in self.opn_ngbhood(v):
            if self.in_t[w] == 0:
                self.__color_edge__(v,w, color_code=1)
                self.parent[w] = v
                self.__depth_search__(w)
            elif self.out_t[w] == 0 and w != self.parent[v]:
                self.__color_edge__(v,w, color_code=2)
        self.t += 1
        self.out_t[v] = self.t

    def __color_edge__(self, v, w, color_code):
        if w < v:
            self.colored_edges[w][v] = color_code
            return
        self.colored_edges[v][w] = color_code