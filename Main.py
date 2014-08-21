__author__ = "Thiago Augustus de Oliveira e Douglas"
__license__ = "GPL"
__version__ = "2.2.4"
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
        for i in range(len(self.nodeList.keys())-1):
            self.setNextNodes()
            self.currentNode = self.getNextNode()
            self.nodeList[self.currentNode].setChecked
            print("Nó selecionado",self.currentNode)

    def setNextNodes(self):
        for item in self.json['vertices']:
            # Current Node exist?
            if self.currentNode == self.json['vertices'][item][0]:
                # Isn't the next node visited?
                if not self.nodeList[self.json['vertices'][item][1]].isChecked:
                    # Is the next node value infinity?
                    if self.nodeList[self.json['vertices'][item][1]].getNodeValue == float('inf'):
                        #
                        self.nodeList[self.json['vertices'][item][1]].setValue(self.json['vertices'][item][2])
                        self.nodeList[self.json['vertices'][item][1]].setParent(self.nodeList[self.currentNode])
                    #
                    else:
                        print("Tinha que ter entrado aqui!!!", self.nodeList[self.json['vertices'][item][1]].getNode)
            # Current Node exits?
            elif self.currentNode == self.json['vertices'][item][1]:
                 # Isn't the next node visited?
                if not self.nodeList[self.json['vertices'][item][0]].isChecked:
                    # Is the next node value infinity?
                    if self.nodeList[self.json['vertices'][item][0]].getNodeValue == float('inf'):
                        #
                        self.nodeList[self.json['vertices'][item][0]].setValue(self.json['vertices'][item][2])
                        self.nodeList[self.json['vertices'][item][0]].setParent(self.nodeList[self.currentNode])
                    #
                    else:
                        print("Tinha que ter entrado aqui!!!", self.nodeList[self.json['vertices'][item][0]].getNode)

    def getNextNode(self) -> object:

        nextNode = None
        #
        for node in self.nodeList:
            #
            if not self.nodeList[node].isChecked:
                #
                if not self.nodeList[node].getNodeValue == float('inf'):
                    #
                    if nextNode is None:
                        nextNode = self.nodeList[node].getNode
                    #
                    elif self.nodeList[node].getValue < self.nodeList[nextNode].getValue:
                        nextNode = self.nodeList[node].getNode
        #
        return nextNode


class Node:

    nodeName = None
    nodeValue = float('inf')
    nodeParent = None
    nodeChecked = False

    def __init__(self, node: object) -> object:
        self.nodeName = node

    @property
    def getNode(self: object):
        return self.nodeName

    def setValue(self, value):
        assert isinstance(value, object)
        self.nodeValue = value

    @property
    def getNodeValue(self: object):
        return self.nodeValue

    @property
    def getValue(self: object):
        if self.nodeParent is not None:
            return self.nodeParent.getValue + self.nodeValue
        return self.nodeValue

    def setParent(self, parent):
        assert isinstance(parent, object)
        if self.nodeParent is None:
            self.nodeParent = parent
        else:
            if parent.getValue < self.nodeParent.getValue:
                self.nodeParent = parent

    @property
    def getParent(self: object):
        return self.nodeParent

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