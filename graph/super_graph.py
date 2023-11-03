
class SuperNode:
    def __init__(self, v):
        self.neighbors = []
        self.value = v
        self.superNode = None
        self.visited = False

    def getEdge(self, v):
        for E in self.neighbors:
            x,y = E.endpts
            if x == v or y == v:
                return E
        return None

    def getNeighbors(self):
        ret = []
        for E in self.neighbors:
            u, v = E.endpts
            if u != self:
                ret.append(u)
            if v != self:
                ret.append(v)
        return ret

    def addNeighbor(self, v, val=None):
        E = SuperEdge(self.value,v,val=val)
        self.addEdge(E)
        return

    def addEdge(self, E):
        self.neighbors.append(E)

class SuperEdge:
    def __init__(self, u, v, val=None):
        self.endpts = (u,v)
        self.value = val

class SuperGraph():
    def __init__(self):
        self.supernodes = []

    def addNode(self, n):
        self.supernodes.append(n)

    def removeNode(self, n):
        self.supernodes.remove(n)
        for E in n.neighbors:
            u,v = E.endpts
            u.neighbors.remove(E)
            v.neighbors.remove(E)
    
    def addEdge(self, u, v, val=None):
        E = SuperEdge(u, v, val=val)
        self.supernodes[u].addEdge(E)
        self.supernodes[v].addEdge(E)

    def getEdges(self):
        ret = []
        for v in self.supernodes:
            v.visited = False
        for v in self.supernodes:
            v.visited = True
            for E in v.neighbors:
                x, y = E.endpts
                if x.visited == False or y.visited == False:
                    ret.append(E)
        return ret
