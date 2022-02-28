class Edge:
    def __init__(self, vertex, cur_flow, capacity, rev):
        self.vertex = vertex  # target vertex
        self.cur_flow = cur_flow  # currently flowing
        self.capacity = capacity  # max capacity
        self.rev = rev  # reverse flow, for the return flow def


class Graph:
    def __init__(self, size, start, sink):
        self.size = size
        self.edges = []
        self.start = start
        self.sink = sink
        self.level = [0 for _ in range(size)]  # 0 means not visited

    def add_edge(self, start, end, capacity):
        edge_a = Edge(end, 0, capacity, len(self.edges[end]))
        edge_b = Edge(start, 0, 0, len(self.edges[start]))

        self.edges.append(edge_a)
        self.edges.append(edge_b)

    def bfs(self, start):
        d = deque()
        d.append(start)
        self.level[start] = 1
        while d:
            u = d.popleft()
            for i in range(self.size):
                if self.edges[u][i]:
                    pass
                # if flow < capacity and not visidet

    def dinic_max_flow(self, start, sink):
        total = 0
        while self.bfs(start, sink):
            while self.return_flow():
                total += 1
        pass


from collections import deque


s = 5


def EdmunKarp():
    flow = 0
    while True:
        q = []  # lista med noder vi bfs:ar
        q

    return flow
