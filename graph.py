"""
Challenge005:
A graph data structure module.
"""


class Graph:
    """
    """

    def __init__(self, graphDict={}):
        """Initializes a graph.
        """
        if graphDict:
            self.__graphDict = graphDict

    def __iter__(self):
        """returns an iterator for the graph object
        """
        self.__graphIter = iter(self.__graphDict)
        return self.__graphIter

    def __next__(self):
        """returs the next element of the iteration i graph.
        the next object.
        """
        return next(self.__graphIter)

    def adjacent(self, x, y):
        """tests whether there is an edge
        from the vertex x to the vertex y;"""
        return (True if y in self.__graphDict[x] else False)

    def neighbors(self, x):
        """lists all vertices y such that there
        is an edge from the vertex x to the vertex y"""
        return self.__graphDict[x]

    def add_vertex(self, x):
        """adds the vertex x, if it is not there"""
        self.__graphDict[x] = {}

    def remove_vertex(self, x):
        """removes the vertex x, if it is there;"""
        self.__graphDict.pop(x)

    def add_edge(self, z):
        """adds the edge z from the vertex x
        to the vertex y, if it is not there;"""
        x, y = tuple(z)
        if x in self.__graphDict:
            if y not in self.__graphDict[x]:
                self.__graphDict[x].add(y)
        else:
            self.__graphDict[x] = {y}

    def remove_edge(self, z):
        """removes the edge z from the vertex
        x to the vertex y, if it is there;"""
        x, y = tuple(z)
        if x in self.__graphDict:
            if y in self.__graphDict[x]:
                self.__graphDict[x].remove(y)

    def get_vertex_value(self, x):
        """returns the value associated
        with the vertex x;"""
        res = set()
        for k, v in self.__graphDict.items():
            if k == x:
                for a in v:
                    if a not in res:
                        res.add(a)
            elif x in v:
                if k not in res:
                    res.add(k)
        return res

    def pathExist(self, x, y):
        """returns if there is a path from the vertex
        x to the vertex y
        using Breadth First Search
        """
        if (x and y) not in self.__graphDict.keys():
            return False
        if self.adjacent(x, y):
            return True
        visited, inQu = {}, []
        for k in self.__graphDict.keys():
            visited[k] = False
        visited[x] = True
        inQu.append(x)
        while inQu:
            val = inQu.pop(0)
            if val == y:
                return True
            for v in self.__graphDict[val]:
                if visited[v] is False:
                    visited[v] = True
                    inQu.append(v)
        return False
    """def set_vertex_value(self, x, v):
        '''sets the value associated
        with the vertex x to v.'''

    def get_edge_value(self, x, y):
        '''returns the value associated with the edge (x, y);'''

    def set_edge_value(self, x, y, v):
        '''sets the value associated with the edge (x, y) to v.'''
    """


if __name__ == "__main__":
    g = {
        "a": {"c"}, "b": {"c", "e"},
        "c": {"a", "b", "d", "e"},
        "d": {"c"}, "e": {"c", "b"},
        "f": {}}
    graph = Graph(g)
    """
    print(graph.neighbors('e'))
    graph.add_edge(("e", "a"))
    graph.add_edge(("e", "a"))
    print(graph.neighbors('e'))
    graph.add_edge(("g", "a"))
    print(graph.neighbors('g'))
    graph.remove_edge(("e", "a"))
    print(graph.neighbors('e'))
    print(graph.get_vertex_value("b"))
    print(graph.pathExist("a", "e"))
    print(graph.pathExist("a", "f"))
    print(graph.pathExist("a", "g"))
    print(graph.pathExist("e", "b"))
    """
