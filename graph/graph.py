from re import finditer 

# grafo com busca em largura e profundidade (bfs e dfs)
class Graph:
    def __init__(self, path=None, data=None):
        self._n = 0
        self._adj_matrix = list()
        self._adj_list = list()
        self._t = 0
        if path:
            self.__load_file__(path)
        elif data:
            self.__load_data__(data)
    
    def get_n(self) -> int:
        return self._n
    
    def get_nodes(self) -> list:
        return [n for n in range(self.get_n())]

    def get_edges(self) -> list:
        edges = list()
        for i in range(self.get_n()):
            for j in range(i, self.get_n()):
                edges.append((i,j)) if self.is_adj(i,j) else None
        return edges

    def get_adj_list_as_dict(self):
        l = self.get_adj_l()
        for n in range(self._n):
            for v in range(len(l[n])):
                l[n][v] += 1
        ret = {n+1: l[n] for n in range(self._n)}
        return ret;

    def get_adj_m(self):
        return self._adj_matrix
    
    def get_adj_l(self):
        return self._adj_list

    def get_degree(self, v):
        return len(self._adj_list[v])

    def get_delta_max(self):
        max = self.get_degree(0)
        for i in range(1, self._n):
            aux = self.get_degree(i)
            if aux >= max:
                max = aux
        return max

    def get_delta_min(self):
        min = self.get_degree(0)
        for i in range(1, self._n):
            aux = self.get_degree(i)
            if aux <= min:
                min = aux
        return min

    def get_degrees(self)->list:
        l = list()
        for i in range(self._n):
            l.append(self.get_degree(i))
        return sorted(l)

    def get_o_ngbhood(self, v):
        return self._adj_list[v]

    def get_c_ngbhood(self, v):
        aux = self._adj_list[v]
        aux.insert(v, v)
        return aux

    def get_regularity(self):
        first_degree = self.get_degree(0)
        for i in range(1, self._n):
            if first_degree != self.get_degree(i):
                return -1
        return first_degree

    def get_universal_nodes(self):
        out = list()
        for i in range(self._n):
            if self.get_degree(i) == self._n-1:
                out.append(i)
        return out
    
    def get_isolated_nodes(self):
        out = list()
        for i in range(self._n):
            if self.get_degree(i) == 0:
                out.append(i)
        return out

    def get_complement(self, g):
        data = list()
        for i in range(self._n):
            data.append(list())
            for j in range(self._n): 
                data[i].append(0 if j == i else 1-g.adj_matrix[i][j])
        return Graph(data=data)

    def get_dist(self, v, w):
        node_lvl = self.search_bfs(v)
        return node_lvl[w]

    def get_node_eccentricity(self, v):
        node_lvl = self.search_bfs(v)
        eccentricity = max(node_lvl)
        return eccentricity
    
    def get_eccentricity_list(self):
        e_list = list()
        for v in range(self._n):
            e_list.append(self.get_node_eccentricity(v))
        return e_list

    def get_radius(self):
        return min(self.get_eccentricity_list())
    
    def get_diameter(self):
        return max(self.get_eccentricity_list())

    def get_apl(self): #average path length
        sum1 = 0
        sum2 = 0
        for v in range(self._n):
            for lvl in self.search_bfs(v):
                sum1 += lvl
            sum1 /= self._n-1
            sum2 += sum1
            sum1 = 0
        return sum2/self._n

    def is_adj(self, a, b):
        if (a > self._n) or (b > self._n):
            return False
        return self._adj_matrix[a][b] == 1

    def is_complete(self):
        max_edges = (self._n*(self._n-1)/2)
        current_edges = 0
        for i in range(1, self._n):
            current_edges += self.get_degree(i)
        current_edges /= 2
        return current_edges == max_edges

    def is_sub(self, n, m):
        if len(n) > self._n:
            return False
        for i in n:
            if i > self._n:
                return False
        for v in m:
            if v[0] | v[1] > self._n:
                return False
            if not self.is_adj(v[0], v[1]):
                return False
        return True

    def is_ride(self, n):
        for i in range(self._n):
            if not self.is_adj(n[i], n[i+1]):
                return False
        return True
    
    def is_way(self, n):
        if not self.is_ride(n):
            return False
        for i in range(self._n-1):
            for j in range(i, self._n):
                if n[i] == n[j]:
                    return False
        return True
    
    def is_cicle(self, n):
        if n[0] != n[len(n)-1]:
            return False
        if not self.is_ride(n):
            return False
        for i in range(self._n-1):
            for j in range(i+1, self._n-1):
                if n[i] == n[j]:
                    return False
        return True

    def is_clique(self, n):
        for i in range(self._n-1):
            for j in range(i+1, self._n):
                if self.is_adj(n[i], n[j]):
                    return False
        return True
    
    def is_independent(self, n):
        return self.get_complement(self).is_cicle(n)

    def search_bfs(self, v, get_colors=False) -> list:
        t = 0
        queue = list()
        entry_t = [0]*self._n
        parent = [0]*self._n
        node_lvl = [-1 for _ in range(self._n) ]
        colors = list()
        for _ in range(self._n):
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
                        colors = self.__color_edge__(colors,v,w,"'0,0,255'")
                        parent[w] = v
                        node_lvl[w] = node_lvl[v]+1
                        t += 1
                        entry_t[w] = t
                        queue.append(w)
                    elif node_lvl[w] == node_lvl[v]:
                        if parent[w] == parent[v]:
                            colors = self.__color_edge__(colors,v,w,"'255,0,0'")
                        else:
                            colors = self.__color_edge__(colors,v,w,"'255,255,0'")
                    elif node_lvl[w] == node_lvl[v]+1:
                        colors = self.__color_edge__(colors,v,w,"'0,255,0'")
        if get_colors:
            return colors
        return node_lvl

    def search_dfs(self, v):
        self._t = 0
        pe = [0]*self._n
        ps = [0]*self._n
        parent = [None]*self._n
        colors = list()
        for c in range(self._n):
            colors.append([None]*self._n)
        self.__depth_search__(v, pe, ps, parent, colors)
        return colors
    
    def __depth_search__(self, v, pe, ps, parent, colors):
        self._t += 1
        pe[v] = self._t
        for w in self.get_o_ngbhood(v):
            if pe[w] == 0:
                colors = self.__color_edge__(colors,v,w,"'0,0,255'")
                parent[w] = v
                self.__depth_search__(w, pe, ps, parent, colors)
            elif ps[w] == 0 and w != parent[v]:
                colors = self.__color_edge__(colors,v,w,"'255,0,0'")
        self._t += 1
        ps[v] = self._t

    def __color_edge__(self, m, v, w, color):
        if v < w:
            m[v][w] = color
        else:
            m[w][v] = color
        return m
    
    def __load_data__(self, data):
        self._n = len(data[0])
        self._adj_matrix = data
        for i in range(self._n):
            self._adj_list.append(list())
            for j in range(self._n):
                if self._adj_matrix[i][j]:
                    self._adj_list[i].append(j)

    def __load_file__(self, path):
        file_iter = open(path, 'r')
        self._n = int(next(file_iter))
        for i in range(self._n):
            self._adj_list.append(list())
            self._adj_matrix.append(list())
            int_iter = finditer("[\\d]", next(file_iter))
            for j in range(self._n):
                is_adj = int(next(int_iter).group())
                self._adj_matrix[i].append(is_adj)
                if is_adj:
                    self._adj_list[i].append(j)
        file_iter.close()