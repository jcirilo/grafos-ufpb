from graph import Graph

class SearchGraph(Graph):
    def __init__(self, path):
        super().__init__(path)

    # TODO
    def deph_search(self, v):
        print(v, self.n)