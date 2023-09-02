import re

class Graph:
    def __init__(self, path=None, data=None):
        self.n = 0
        self.adj_matrix = list()
        self.adj_list = list()

        if data:
            self.n = len(data[0])
            self.adj_matrix = data
            for i in range(self.n):
                self.adj_list.append(list())
                for j in range(self.n):
                    if self.adj_matrix[i][j]:
                        self.adj_list[i].append(j)
        else:
            if path:
                self.load_file(path)

    def load_file(self, path):
        file_iter = open(path, 'r')
        self.n = int(next(file_iter))

        for i in range(self.n):
            self.adj_list.append(list())
            self.adj_matrix.append(list())
            int_iter = re.finditer('[\d]', next(file_iter))

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

    def get_degrees(self):
        sorted = []
        for i in range(self.n):
            sorted.append(self.degree(i))
        sorted.sort()
        return sorted

    def get_open_neighbourhood(self, v):
        return self.adj_list[v]

    def get_closed_neighbourhood(self, v):
        aux = self.adj_list[v]
        aux.append(v)
        return aux

    def is_adjacent(self, a, b):
        if a | b > self.n:
            return False
        return self.adj_matrix[a][b] == 1

    def get_regularity(self):
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

    def get_universal_vertices(self):
        out = list()
        for i in range(self.n):
            if self.degree(i) == self.n-1:
                out.append(i)
        return out
    
    def get_isolated_vertices(self):
        out = list()
        for i in range(self.n):
            if self.degree(i) == 0:
                out.append(i)
        return out
    
    def is_subgraph(self, n, m):
        if len(n) > self.n:
            return False

        for i in n:
            if i > self.n:
                return False

        for v in m:
            if v[0] | v[1] > self.n:
                return False
            if not self.is_adjacent(v[0], v[1]):
                return False

        return True

    def is_ride(self, n):
        for i in range(self.n):
            if not self.is_adjacent(n[i], n[i+1]):
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
                if self.is_adjacent(n[i], n[j]):
                    return False
        return True
    
    def get_complement(self, g):
        data = list()
        
        for i in range(self.n):
            data.append(list())
            for j in range(self.n): 
                data[i].append(0 if j == i else 1-g.adj_matrix[i][j])

        return Graph(data=data)

    def is_independent(self, n):
        return self.get_complement().g.is_cicle(n)
