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
        self.nodeList[self.currentNode].setChecked

        #Call the algorithm
        self.dijkstra()

    def dijkstra(self):

        # Check all nodes length
        for i in range(len(self.nodeList.keys())):
            #print(self.currentNode, i, self.nodeList.get(self.currentNode))
            self.setNextNodes()
            self.currentNode = self.getNextNode()
            self.nodeList[self.currentNode].setChecked
            print(self.currentNode)

    def setNextNodes(self) -> object:
        for item in self.json['vertices']:
            # Check the first node vertice
            if self.json['vertices'][item][0] == self.currentNode and not self.nodeList[self.json['vertices'][item][1]].isChecked:
                if self.json['vertices'][item][2] < self.nodeList[self.json['vertices'][item][1]].getValue:
                    self.nodeList[self.json['vertices'][item][1]].setValue(self.json['vertices'][item][2])
                    self.nodeList[self.json['vertices'][item][1]].setParent(self.nodeList[self.currentNode])
            # Check the second node vertice
            elif self.json['vertices'][item][1] == self.currentNode and not self.nodeList[self.json['vertices'][item][1]].isChecked:
                if self.json['vertices'][item][2] < self.nodeList[self.json['vertices'][item][1]].getValue:
                    self.nodeList[self.json['vertices'][item][0]].setValue(self.json['vertices'][item][2])
                    self.nodeList[self.json['vertices'][item][0]].setParent(self.nodeList[self.currentNode])

    def getNextNode(self) -> object:
        nextNode = None
        for node in self.nodeList:
            if not self.nodeList[node].isChecked:
                if nextNode is None and self.nodeList[node].getValue < float('inf'):
                    nextNode = node
                elif self.nodeList[node].getValue < self.nodeList[nextNode].getValue:
                    nextNode = node

        print(nextNode)


class Node:

    nodeName = None
    nodeValue = float('inf')
    nodeParent = None
    nodeChecked = False

    def __init__(self, node: object) -> object:
        self.node = node

    @property
    def getNode(self: object):
        return self.nodeName

    def setValue(self, value):
        assert isinstance(value, object)
        self.nodeValue = value

    @property
    def getValue(self: object):
        return self.nodeValue

    def setParent(self, parent):
        assert isinstance(parent, object)
        self.nodeParent = parent

    @property
    def setChecked(self: object):
        self.nodeChecked = True

    @property
    def isChecked(self) -> object:
        return self.nodeChecked


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