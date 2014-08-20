__author__ = "Thiago Augustus e Douglas"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "thiagoaugustusdeoliveira@gmail.com"
__status__ = "Production"

import json

class Algorithm:

    path = []
    json = None
    nodeList = {}
    currentNode = None

    def __init__(self, n):

        # Get the json file contents
        self.json = JsonRead().readJson()

        # Create an node list
        for i in self.json['nodes']:
            node = Node(i)
            self.nodeList[i] = node

        # Add the first node
        self.currentNode = self.nodeList.get(n)
        self.currentNode.setValue(0)

        # Call the algorithm
        self.dijkstra()

    def dijkstra(self):

        for i in range(len(self.nodeList.keys())):
            self.currentNode.setVertices(self.getVertices(self.currentNode.getNode()))
            vertice = self.currentNode.getVertice
            newNode = self.nodeList.get(vertice[0])
            newNode.setValue(vertice[1])
            newNode.setParent(self.currentNode)
            self.currentNode.setUnchecked()

    # Method GetVertices return[[nextNode,valueCost]]
    def getVertices(self, node):
        vertices = []
        for item in self.json['vertices']:
            if self.json['vertices'][item][0] == node:
                vertices.append([self.json['vertices'][item][1],self.json['vertices'][item][2]])
            elif self.json['vertices'][item][1] == node:
                vertices.append([self.json['vertices'][item][0],self.json['vertices'][item][2]])
        return vertices


class Node:

    node = None
    parent = None
    vertices = []
    unchecked = True
    value = float('inf')

    def __init__(self, node) -> object:
        self.node = node

    def getNode(self):
        return self.node

    def setParent(self, node: object):
        self.node = node

    @property
    def getParent(self) -> object:
        assert isinstance(self.node, object)
        return self.node

    def setVertices(self, vertices):
        self.vertices = vertices

    @property
    def getVertice(self) -> object:
        lower = [None, float('inf')]
        for vertice in self.vertices:
            if (vertice[1]+self.value) < lower[1]:
                assert isinstance(vertice, object)
                vertice[1] += self.value
                lower = vertice
        return lower

    def setUnchecked(self):
        self.unchecked = False

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class JsonRead:
    def __init__(self):
        pass

    # Read Json Method
    def readJson(self):
        # Open the informed file path
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file


Algorithm('A')