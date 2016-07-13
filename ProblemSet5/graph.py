# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedEdge(Edge):
    def __init__(self, src, dest, tot, out):
        Edge.__init__(self, src, dest)
        self.tot = float(tot)
        self.out = float(out)
    def getTotalDistance(self):
        return self.tot
    def getOutdoorDistance(self):
        return self.out
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.tot, self.out)

class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        tot = edge.getTotalDistance()
        out = edge.getOutdoorDistance()
        if isinstance(src, str):
            src = Node(src)
        if isinstance(dest, str):
            dest = Node(dest)
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest,(tot,out)])
    def childrenOf(self, node):
        return [child[0] for child in self.edges[node]]
    def getNodes(self):
        return self.nodes
    def getEdges(self, nodeID = None):
        if nodeID:
            return self.edges[Node(nodeID)]
        else:
            return self.edges
    def getDistances(self, src, dest):
        edges = self.getEdges(src)
        for edge in edges:
            if edge[0] == dest:
                dists = (edge[1][0], edge[1][1])
        return dists
    def __str__(self):
        res = ''
        for k in self.edges:
            for edge in self.edges[k]:
                d = edge[0]
                t = float(edge[1][0])
                o = float(edge[1][1])
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d, t, o)
        return res[:-1]
