# Kruskals Algorithm implementation
# ∀ u, v  V, u = (x1,y1), v = (x2,y2)
# w(u,v) = d(u, v) = 𝑛𝑒𝑎𝑟𝑒𝑠𝑡𝑖𝑛𝑡 √(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2
import heapq
import itertools
import math


# Disjoint set
# Union - Find
class Set:
    def __init__(self):
        self.set = []

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
        self.sets = [[]]*2
        self.g = []

    def add_vertex(self, x, y):
        self.g.append([x, y])

    def find_sets(self):
        for i in itertools.combinations(self.g, 2):
            self.sets[0].append(i)
            self.sets[1].append(-1)
            # s = Set()
            # s.union(i[0], i[1])
            # self.sets.append(s)

    def find_edge_distance(self):
        for i, set_ in enumerate(self.sets[0]):
            if i % 2 == 1:
                continue
            print("set in edge: ", set_)
            print(i)
            d = calc_distance(set_[0])
            self.sets[1][i] = d



def calc_distance(set_):
    [x1, y1] = set_[0]
    x2, y2 = set_[1]
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    print(distance)
    return distance


# extract data from graph.txt
def read_file():
    lines = []
    with open('graph.txt', 'r') as r:
        lines = [line.rstrip() for line in r]
    return lines


# process data from the files
def process_lines(lines):
    # t: number of test cases
    t = int(lines[0])
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
            g.add_vertex(int(v[0]), int(v[1]))
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
    test_cases_[0].find_sets()
    test_cases_[0].find_edge_distance()
    calc_distance(test_cases_[0].sets[0][0])


if __name__=="__main__":
    main()

