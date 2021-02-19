# Kruskals Algorithm implementation
# ∀ u, v  V, u = (x1,y1), v = (x2,y2)
# w(u,v) = d(u, v) = 𝑛𝑒𝑎𝑟𝑒𝑠𝑡𝑖𝑛𝑡 √(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2
import heapq

# Disjoint set
# Union - Find
class Set:
    def __init__(self, n):
        self.set = [-1]*n

    def union(self, root1, root2):
        if self.set[root1] < self.set[root2]:
            self.set[root1] = root2
        else:
            if self.set[root1] == self.set[root2]:
                self.set[root1] -= 1
            self.set[root2] = root1

    def find(self, x):
        if self.set[x] < 0:
            return x
        n = 0
        while self.set[n] > 0:
            n = self.set[n]
        return n




class Graph:
    # _k: number of vertices
    # g: graph, adjacency matrix implementation
    # sets: list of disjoint sets
    def __init__(self, _k):
        self._k = _k
        self.sets = []
        self.g = []*_k

    def add_vertex(self, x, y):
        self.g.append([x, y])


# extract data from graph.txt
def read_file():
    with 




def kruskal():
    s = Set()

    i = 0


def main():



if __name__=="__main__":
    main()

