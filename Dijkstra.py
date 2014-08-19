__author__ = 'ThiagoAugustus'

import copy
import json

class DijkstraAlgorithm:

    file = None
    visited = []
    unvisited = []
    current = None
    iteration = {}

    # Constructor Method
    def __init__(self, node = None):
        self.file = self.readJson() # Read the json file
        self.dijkstra(self.file,node) # Invoke the algorithm

    # Dijkstra Algorithm Core
    def dijkstra(self, graph, node = None):

        self.unvisited = self.file['nodes'] # Set all unvisited nodes

        # Verify is the starting node was informed
        if node == None:
            self.current = self.unvisited.pop() # Choose an aleatory node
        else:
            self.current = node

        # Fill with the first visited node
        self.visited.append(self.current)

        # Goes on all nodes
        while self.unvisited:
            #print(self.visited)
            self.mountIteration(self.file['nodes'], self.current)
            self.unvisited.pop()
            #self.visited.append(self.current)
            print(self.iteration)

    # Mount the table iteration with node cost Method
    def mountIteration(self, nodes, node):
        for n in nodes:
            if self.iteration.get(n) == None:
                # Add the intial values [value,parent]
                if n == node:
                    self.iteration[n] = [0,None]
                else:
                    self.iteration[n] = [float("inf"),None]
            else:
                tempNode = self.expand(node, n)
                if tempNode != None:
                    if tempNode[0] < self.iteration[n][0]:
                        self.iteration[n] = tempNode
                pass

    # Expand Node Method
    def expand(self, nodeFrom, nodeTo):
        for item in self.file['vertices'].keys():
            if self.file['vertices'][item][0] == nodeFrom and self.file['vertices'][item][1] == nodeTo:
                return [self.file['vertices'][item][2],self.file['vertices'][item][0]]
            elif self.file['vertices'][item][1] == nodeFrom and self.file['vertices'][item][0] == nodeTo:
                return [self.file['vertices'][item][2],self.file['vertices'][item][1]]
        return None

    # Read Json Method
    def readJson(self):
        # Open the informed file path
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file

DijkstraAlgorithm('A')