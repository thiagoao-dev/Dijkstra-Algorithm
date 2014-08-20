__author__ = "Thiago Augustus de Oliveira e Douglas"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "thiagoaugustusdeoliveira@gmail.com"
__status__ = "Production"

import json


class Algorithm:

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

        #Call the algorithm
        self.dijkstra()

    def dijkstra(self):

        # Check all nodes length
        for i in range(len(self.nodeList.keys())):
            self.json['vertices']
            print(self.currentNode, i, self.nodeList.get(self.currentNode))
            pass

    #Method GetVertices return[[nextNode,valueCost]]
    def getVertices(self, node):
        vertices = []
        for item in self.json['vertices']:
            if self.json['vertices'][item][0] == node and not self.nodeList[self.json['vertices'][item][1]].isChecked:
                vertices.append([self.json['vertices'][item][1], self.json['vertices'][item][2]])
            elif self.json['vertices'][item][1] == node and not self.nodeList[self.json['vertices'][item][0]].isChecked:
                vertices.append([self.json['vertices'][item][0], self.json['vertices'][item][2]])
        return vertices


class Node:
    nodeName = None
    nodeValue = float('inf')
    nodeParent = None
    nodeChecked = False

    def __init__(self, node: object) -> object:
        self.node = node

    def setValue(self, value):
        assert isinstance(value, object)
        self.nodeValue = value

    def setParent(self, parent):
        assert isinstance(parent, object)
        self.nodeParent = parent

    def setChecked(self):
        self.nodeChecked = True


class JsonRead:
    def __init__(self):
        pass

    # Read Json Method
    @staticmethod
    def readJson() -> object:
        """
        Return a dictionary
        :rtype : object
        """
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file


Algorithm('A')