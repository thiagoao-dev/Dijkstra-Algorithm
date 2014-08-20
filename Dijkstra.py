__author__ = "Thiago Augustus de Oliveira"
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

        # Call the algorithm
        self.dijkstra()

    def dijkstra(self):

        for i in range(len(self.nodeList.keys())):
            self.currentNode.setVertices(self.getVertices(self.currentNode.getNode()))

    def getVertices(self, node):
        print(node)
        pass


class Node:
    node = None
    parent = None
    vertices = []
    unchecked = True
    value = float('inf')

    def __init__(self, node):
        self.node = node

    def getNode(self):
        return self.node

    def setParent(self, node):
        self.node = node

    def getParent(self):
        return self.node

    def setVertices(self, vertices):
        self.vertices = vertices

    def getVertices(self, minor=False):
        pass

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


class DijkstraAlgorithm:
    file = None
    visited = []
    unvisited = []
    current = None
    iteration = {}
    nodesList = []

    # Constructor Method
    def __init__(self, node=None):

        self.file = self.readJson()  # Read the json file

        for node in self.file['nodes']:
            print(node)
            n = Node(node)
            self.nodesList.append(node)
            print(self.nodesList[0])

        self.dijkstra(self.file, node)  # Invoke the algorithm

    # Dijkstra Algorithm Core
    def dijkstra(self, graph, node=None):

        self.unvisited = self.file['nodes']  # Set all unvisited nodes

        # Verify is the starting node was informed
        if node == None:
            self.current = self.unvisited.pop()  # Choose an aleatory node
        else:
            self.current = node

        # Fill with the first visited node
        self.visited.append(self.current)
        self.mountIteration(self.file['nodes'], self.current)[1]
        # print('Nó escolhido',self.current)
        # Goes on all nodes
        while self.unvisited:
            #self.mountIteration(self.file['nodes'], self.current)
            self.current = self.mountIteration(self.file['nodes'], self.current)[1]
            self.visited.append(self.current)
            self.unvisited.pop()
            #print('Nó escolhido',self.current)
            #print(self.iteration)

    # Mount the table iteration with node cost Method
    def mountIteration(self, nodes, node):

        smallNodeValue = [float('inf'), None]

        for n in nodes:
            if self.iteration.get(n) == None:
                # Add the intial values [value,parent]
                if n == node:
                    self.iteration[n] = [0, None]
                else:
                    self.iteration[n] = [float("inf"), None]
            else:
                tempNode = self.expand(node, n)
                if tempNode != None and n not in self.visited:

                    if tempNode[0] < smallNodeValue[0]:
                        smallNodeValue = tempNode

                    if tempNode[0] < self.iteration[n][0]:
                        self.iteration[n] = [tempNode[0], node]

        return smallNodeValue

    # Expand Node Method
    def expand(self, nodeFrom, nodeTo):
        for item in self.file['vertices'].keys():
            if self.file['vertices'][item][0] == nodeFrom and self.file['vertices'][item][1] == nodeTo:
                # if self.file['vertices'][item][1] not in self.visited:
                return [self.file['vertices'][item][2], self.file['vertices'][item][1]]
            elif self.file['vertices'][item][1] == nodeFrom and self.file['vertices'][item][0] == nodeTo:
                # if self.file['vertices'][item][0] not in self.visited:
                return [self.file['vertices'][item][2], self.file['vertices'][item][0]]
        return None

    # Read Json Method
    def readJson(self):
        # Open the informed file path
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file

            #DijkstraAlgorithm('A')