# Kruskals Algorithm implementation
# ∀ u, v  V, u = (x1,y1), v = (x2,y2)
# w(u,v) = d(u, v) = 𝑛𝑒𝑎𝑟𝑒𝑠𝑡𝑖𝑛𝑡 √(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2
import itertools # Used to find all possible sets
import math


# Disjoint set
# Union - Find
class Set:
    # set: disjoint set of vertices
    # ln: length of set
    def __init__(self, n):
        self.set = [-1]*n
        self.ln = 0

    # Create a union of two sets
    def union(self, v1, v2):
        if self.set[v1] < self.set[v2]:
            self.set[v1] = v2
        else:
            if self.set[v1] == self.set[v1]:
                self.set[v1] -= 1
            self.set[v2] = v1
        self.ln += 1

    # Find value in set
    def find(self, r):
        x = r[0] + r[1]
        if self.set[x] < 0:
            return x
        n = 0
        while self.set[n] > 0:
            n = self.set[n]
        return n


# Definition of graph
class Graph:
    # _k: number of vertices
    # g: graph, adjacency matrix implementation
    # sets: list of disjoint sets
    def __init__(self, _k):
        self._k = _k
        self.sets = {}
        self.g = []

    # Add a vertex to graph
    def add_vertex(self, x, y):
        self.g.append([x, y])

    # help sort, return calculation to sort by
    def help_sort(self, s):
        d = calc_distance(s[0])
        return d

    # Go through graph and find all possible sets
    def find_sets(self):
        idx = 0
        s = {}
        # Itertool.combinations finds all possible sets
        for i in itertools.combinations(self.g, 2):
            c = calc_distance(i)
            # add sets to a dict.
            p = {idx: [i, c]}
            s.update(p)
            idx += 1
        self.sets = [val for key, val in s.items() if val != -1]
        # Move sets to sorted list
        # No need to have it put in a dict first, too lazy to remove it..
        self.sets.sort(key=self.help_sort)

    # Kruskal's algorithm implementation
    def kruskal(self):
        # store already used sets
        vertex_sets = Set(self._k*100)
        # Store edges that are used in soln
        res = []
        i = 0
        # Sore edge weight used in soln
        mst_edges = []

        # Loop till
        while i < len(self.sets) and vertex_sets.ln < self._k-1:
            curr_edge = self.sets[i]

            v1 = vertex_sets.find(curr_edge[0][0])
            v2 = vertex_sets.find(curr_edge[0][1])

            # check if next vertex can be added to mst
            if v1 != v2:
                mst_edges.append(curr_edge[1])
                res.append(curr_edge)
                vertex_sets.union(v1, v2)
            i += 1
        min_cost = 0

        print("Edges in MST")
        print("Distance              Point (x, y)")
        for weight in range(0, len(mst_edges)):
            min_cost += mst_edges[weight]
            print_edge(res[weight])
        print("Total distance: ", min_cost)


# Print out vertex set in mst with distance
def print_edge(e):
    x1, y1 = e[0][0]
    x2, y2 = e[0][1]
    weight = e[1]
    print(str(weight)+"                     (" + str(x1)
          + ", " + str(y1) + ")  -   (" + str(x2) + ", " + str(y2) + ")")


# Calculate euclidean distance
def calc_distance(set_):
    x1, y1 = set_[0]
    x2, y2 = set_[1]
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
        # loop through ordered pairs and put in graph
        for k in range(i + 1, k + i + 1):
            v = lines[k].split()
            # Add vertex x,y points to graph
            g.add_vertex(int(v[0]), int(v[1]))
        # Shift i to move to next graph
        i = k + 1
        curr += 1
        test_cases.append(g)
    return test_cases


# driver
def main():
    test_cases_ = process_lines(read_file())

    for i in range(0, len(test_cases_)):
        print("Test case: ", i+1)
        test_cases_[i].find_sets()
        test_cases_[i].kruskal()
        print()


if __name__=="__main__":
    main()

