# Kruskals Algorithm implementation
# ∀ u, v  V, u = (x1,y1), v = (x2,y2)
# w(u,v) = d(u, v) = 𝑛𝑒𝑎𝑟𝑒𝑠𝑡𝑖𝑛𝑡 √(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2
import heapq
import itertools
import math


# Disjoint set
# Union - Find
class Set:
    def __init__(self, n):
        self.set = [-1]*n
        self.ln = 0

    def union(self, r1, r2):

        if self.set[r1] < self.set[r2]:
            self.set[r1] = r2
        else:
            if self.set[r1] == self.set[r1]:
                self.set[r1] -= 1
            self.set[r2] = r1
        self.ln += 1

    def find(self, r):
        x = r[0] + r[1]
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
        self.sets = {}
        self.g = []

    def add_vertex(self, x, y):
        heapq.heappush(self.g, [x, y])
        #self.g.append([x, y])

    def help_sort(self, s):
        d = calc_distance(s[0], 1)
        return d

    def find_sets(self):
        idx = 0
        s = {}
        for i in itertools.combinations(self.g, 2):
            c = calc_distance(i, idx)
            p = {idx: [i, c]}
            s.update(p)
            idx += 1
        self.sets = [val for key, val in s.items() if val != -1]
        self.sets.sort(key=self.help_sort)


    def kruskal(self):
        vertex_sets = Set(self._k*100)
        res = []
        i = 0
        j = 0
        mst_edges = []
        # = [k for k in self.sets]

        while i < len(self.sets) and vertex_sets.ln < self._k-1:
            curr_edge = self.sets[i]

            r1 = vertex_sets.find(curr_edge[0][0])
            r2 = vertex_sets.find(curr_edge[0][1])

            if r1 != r2:
                mst_edges.append(curr_edge[1])
                res.append(curr_edge)
                vertex_sets.union(r1, r2)

            i += 1
        min_cost = 0
        print("Edges in MST")
        print("Distance              Point (x, y)")
        for weight in range(0, len(mst_edges)):
            min_cost += mst_edges[weight]
            print_edge(res[weight])

        print("Total distance: ", min_cost)

def print_edge(e):
    x1, y1 = e[0][0]
    x2, y2 = e[0][1]
    weight = e[1]
    print(str(weight)+"                     (" + str(x1) + ", " + str(y1) + ")  -   (" + str(x2) + ", " + str(y2) + ")")




def calc_distance(set_, key):
    #s1, s2 = set_[key][0]
    x1, y1 = set_[0]#, s1[1]
    x2, y2 = set_[1]#, s2[1]
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return round(distance)


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


def main():
    test_cases_ = process_lines(read_file())

    # test_cases_[1].find_sets()
    # #test_cases_[0].find_edge_distance()
    # print("___________________")
    # from pprint import pprint
    # pprint(test_cases_[1].sets)
    # print("____________________")
    # test_cases_[1].kruskal()

    for i in range(0, len(test_cases_)):
        print("Test case: ", i+1)
        test_cases_[i].find_sets()
        #test_cases_[0].find_edge_distance()
        test_cases_[i].kruskal()
        print()


if __name__=="__main__":
    main()

