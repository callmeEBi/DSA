class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, *vertices):
        for vertex in vertices:
            if vertex not in self.adj_list:
                self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            return False
        if v2 in self.adj_list[v1] or v1 in self.adj_list[v2]:
            return False
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True


my_graph = Graph()
my_graph.add_vertex("a", "b", "c", "d")
my_graph.add_edge("a", "b")
my_graph.add_edge("a", "c")
my_graph.add_edge("a", "d")
my_graph.add_edge("b", "d")
my_graph.add_edge("c", "d")
my_graph.print_graph()
