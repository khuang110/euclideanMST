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
        self.g = []

    def add_vertex(self, x, y):
        self.g.append([x, y])


# extract data from graph.txt
def read_file():
    lines = []
    with open('graph.txt', 'r') as r:
        lines = [line.rstrip() for line in r]
    return lines


# process data from the files
def process_lines(lines):
    itr = iter(lines)
    # t: number of test cases
    t = int(next(itr))
    test_cases = []
    curr = 0
    i = 1
    while i < len(lines) and curr < t:
        # k: number of vertices
        k = int(lines[i])

        g = Graph(k)
        for k in range(i + 1, k + i + 1):
            v = lines[k].split()
            # Add vertex x,y points to graph
            g.add_vertex(v[0], v[1])
        # Shift i to move to next graph
        i = k + 1
        curr += 1
        test_cases.append(g)
    return test_cases



def kruskal():
    s = Set()
    i = 0


def main():
    test_cases_ = process_lines(read_file())



if __name__=="__main__":
    main()

