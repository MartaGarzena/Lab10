import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listCountryCode = []
        self._listConfini = []
        self._listCountry = []

        self._listAllCountry = DAO.getAllNodes()

        self._idNoMapCountry = {}
        for a in self._listAllCountry:
            self._idNoMapCountry[a.CCode] = a

        self.grafo = nx.Graph()

    @property
    def listCountry(self):
        return self._listAllCountry

    def getNumNodi(self):
        return len(self.grafo.nodes)

    def getNumArchi(self):
        return len(self.grafo.edges)

    def buildGraph(self, year):
        self._listConfini = DAO.getEdgeFromYear(year)
        self._listCountryCode = DAO.getNodesFromYear(year)

        for code in self._listCountryCode:
            self._listCountry.append(self._idNoMapCountry[code])

        self.grafo.add_nodes_from(self._idNoMapCountry.values())
        self.addEdges()

    def addEdges(self):
        allEdges = self._listConfini
        for arc in allEdges:
            u = self._idNoMapCountry[arc.state1no]
            v = self._idNoMapCountry[arc.state2no]
            self.grafo.add_edge(u, v)
