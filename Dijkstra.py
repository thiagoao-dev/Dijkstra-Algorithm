__author__ = "Thiago Augustus de Oliveira e Douglas"
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
        self.currentNode = n
        self.nodeList[self.currentNode].setValue(0)

        # Call the algorithm
        self.dijkstra()

    def dijkstra(self):

        # Check all nodes length
        for i in range(len(self.nodeList.keys())):
            # Set the node vertices
            self.nodeList[self.currentNode].setVertices(self.getVertices(self.nodeList[self.currentNode].getNode))
            # Return a node with smallest value [nextNode, value]
            vertice = self.nodeList[self.currentNode].getVertice
            newNode = self.nodeList.get(vertice[0])
            print(self.currentNode, newNode.getNode)
            newNode.setValue(vertice[1])
            newNode.setParent(self.nodeList[self.currentNode])
            self.nodeList[self.currentNode].setUnchecked
            self.currentNode = newNode.getNode

    # Method GetVertices return[[nextNode,valueCost]]
    def getVertices(self, node):
        vertices = []
        for item in self.json['vertices']:
            if self.json['vertices'][item][0] == node and not self.nodeList[self.json['vertices'][item][1]].isChecked:
                vertices.append([self.json['vertices'][item][1], self.json['vertices'][item][2]])
            elif self.json['vertices'][item][1] == node and not self.nodeList[self.json['vertices'][item][0]].isChecked:
                vertices.append([self.json['vertices'][item][0], self.json['vertices'][item][2]])
        return vertices


class Node:
    node = None
    parent = None
    vertices = []
    checked = False
    value = float('inf')

    def __init__(self, node: object) -> object:
        self.node = node

    @property
    def getNode(self: object):
        assert isinstance(self.node, object)
        return self.node

    def setParent(self, parent: object):
        self.parent = parent

    @property
    def getParent(self) -> object:
        assert isinstance(self.parent, object)
        return self.parent

    def setVertices(self, vertices):
        self.vertices = vertices

    @property
    def getVertice(self) -> object:
        lower = [None, float('inf')]
        for vertice in self.vertices:
            if (vertice[1] + self.value) < lower[1]:
                assert isinstance(vertice, object)
                vertice[1] += self.value
                lower = vertice
        return lower

    @property
    def setUnchecked(self) -> object:
        self.checked = True

    @property
    def isChecked(self) -> object:
        assert isinstance(self.checked, object)
        return self.checked

    def setValue(self, value):
        assert isinstance(value, object)
        self.value = value

    @property
    def getValue(self) -> object:
        assert isinstance(self.value, object)
        assert isinstance(self.parent, object)
        # Check if the node have parent node
        if self.parent is not None:
            return self.value + self.parent.getValue
        else:
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