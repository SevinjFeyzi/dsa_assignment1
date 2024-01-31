

class Graph:
    def __init__(self, nofverts):
        """
        Initializes a graph with the given number of vertices.

        Parameters:
        - nofverts (int): The number of vertices in the graph.
        """
        self.graph = [[] for _ in range(nofverts)]

    def add_vertex(self):
        """
        Adds a new vertex to the graph.

        Returns:
        - bool: True if the vertex is added successfully, False otherwise.
        """
        li = []
        self.graph.append(li)

    def add_edge(self, idx, sndidx, weight=1):
        """
        Adds an edge between two vertices with an optional weight.

        Parameters:
        - idx (int): The index of the first vertex.
        - sndidx (int): The index of the second vertex.
        - weight (int): The weight of the edge (default is 1).

        Returns:
        - bool: True if the edge is added successfully, False otherwise.
        """
        if idx < 0 or idx >= len(self.graph) or sndidx < 0 or sndidx >= len(self.graph):
            return False

        for edge in self.graph[idx]:
            if sndidx == edge[0]:
                return False

        self.graph[idx].append((sndidx, weight))
        return True

    def has_edge(self, idx, sndidx):
        """
        Checks if there is an edge between two vertices.

        Parameters:
        - idx (int): The index of the first vertex.
        - sndidx (int): The index of the second vertex.

        Returns:
        - bool: True if there is an edge, False otherwise.
        """
        if idx < 0 or idx >= len(self.graph) or sndidx < 0 or sndidx >= len(self.graph):
            return False

        for edge in self.graph[idx]:
            if edge[0] == sndidx:
                return True

        return False

    def edge_weight(self, idx, sndidx):
        """
        Returns the weight of the edge between two vertices.

        Parameters:
        - idx (int): The index of the first vertex.
        - sndidx (int): The index of the second vertex.

        Returns:
        - int or None: The weight of the edge if it exists, None otherwise.
        """
        if idx < 0 or idx >= len(self.graph) or sndidx < 0 or sndidx >= len(self.graph):
            return None

        for edge in self.graph[idx]:
            if edge[0] == sndidx:
                return edge[1]

        return None

    def num_edges(self):
        """
        Returns the total number of edges in the graph.

        Returns:
        - int: The number of edges.
        """
        count = 0
        for edges in self.graph:
            count += len(edges)
        return count

    def num_verts(self):
        """
        Returns the total number of vertices in the graph.

        Returns:
        - int: The number of vertices.
        """
        return len(self.graph)

    def get_connected(self, v):
        """
        Returns a list of vertices connected to the given vertex.

        Parameters:
        - v (int): The index of the vertex.

        Returns:
        - list: A list of connected vertices.
        """
        if v < 0 or v >= len(self.graph):
            return []

        return self.graph[v]


class LabelGraph:
    def __init__(self, vertex_list):
        """
        Initializes a labeled graph with the given list of vertices.

        Parameters:
        - vertex_list (list): List of vertex names.
        """
        self.graph = [[] for _ in range(len(vertex_list))]
        self.vertices = dict(zip(vertex_list, range(len(vertex_list))))

    def add_vertex(self, vertex_name):
        """
        Adds a new vertex to the labeled graph.

        Parameters:
        - vertex_name (str): The name of the vertex.

        Returns:
        - bool: True if the vertex is added successfully, False otherwise.
        """
        if vertex_name not in self.vertices:
            self.vertices[vertex_name] = len(self.graph)
            self.graph.append([])
            return True
        return False

    def add_edge(self, from_vertex, to_vertex, weight=1):
        """
        Adds an edge between two vertices with an optional weight.

        Parameters:
        - from_vertex (str): The name of the first vertex.
        - to_vertex (str): The name of the second vertex.
        - weight (int): The weight of the edge (default is 1).

        Returns:
        - bool: True if the edge is added successfully, False otherwise.
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False

        idx_from = self.vertices[from_vertex]
        idx_to = self.vertices[to_vertex]

        for edge in self.graph[idx_from]:
            if idx_to == edge[0]:
                return False

        self.graph[idx_from].append((idx_to, weight))
        return True

    def num_edges(self):
        """
        Returns the total number of edges in the labeled graph.

        Returns:
        - int: The number of edges.
        """
        count = 0
        for edges in self.graph:
            count += len(edges)
        return count

    def num_verts(self):
        """
        Returns the total number of vertices in the labeled graph.

        Returns:
        - int: The number of vertices.
        """
        return len(self.graph)

    def get_verts(self):
        """
        Returns a list of vertex names in the labeled graph.

        Returns:
        - list: A list of vertex names.
        """
        return list(self.vertices.keys())

    def has_edge(self, from_vertex, to_vertex):
        """
        Checks if there is an edge between two vertices.

        Parameters:
        - from_vertex (str): The name of the first vertex.
        - to_vertex (str): The name of the second vertex.

        Returns:
        - bool: True if there is an edge, False otherwise.
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False

        idx_from = self.vertices[from_vertex]
        idx_to = self.vertices[to_vertex]

        for edge in self.graph[idx_from]:
            if idx_to == edge[0]:
                return True

        return False

    def edge_weight(self, from_vertex, to_vertex):
        """
        Returns the weight of the edge between two vertices.

        Parameters:
        - from_vertex (str): The name of the first vertex.
        - to_vertex (str): The name of the second vertex.

        Returns:
        - int or None: The weight of the edge if it exists, None otherwise.
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return None

        idx_from = self.vertices[from_vertex]
        idx_to = self.vertices[to_vertex]

        for edge in self.graph[idx_from]:
            if idx_to == edge[0]:
                return edge[1]

        return None

    def get_connected(self, from_vertex):
        """
        Returns a list of vertices connected to the given vertex.

        Parameters:
        - from_vertex (str): The name of the vertex.

        Returns:
        - list: A list of connected
        """
        if from_vertex not in self.vertices:
            return []

        idx_from = self.vertices[from_vertex]
        connected = [(self.get_verts()[edge[0]], edge[1]) for edge in self.graph[idx_from]]
        return connected
