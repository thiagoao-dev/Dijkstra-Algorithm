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

        self.unvisited = self.file['nodes'] # Set all ndoes

        # Verify is the starting node was informed
        if node == None:
            self.current = self.unvisited.pop() # Choose an aleatory node
        else:
            self.current = node

        # Fill with the first visited node
        self.visited.append(self.current)

        # Goes on all nodes
        while self.unvisited:
            print(self.visited)
            self.mountIteration(self.file['nodes'], self.current)
            self.expandir(self.file['vertices'], self.current)
            self.current = self.unvisited.pop()
            self.visited.append(self.current)

        pass

    # Read Json Method
    def readJson(self):
        # Open the informed file path
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file

    # Mount the table iteration with node cost Method
    def mountIteration(self, nodes, node):
        for n in nodes:
            # Add custo zero para o nó inicial
            if n == node:
                self.iteration[n] = 0
            else:
                self.iteration[n] = float("inf")

    # Função que retorna as possíveis ações
    def expandir(self, vertices, node):
        # Cria caminhos
        nodes = [] # Armazena vetices e custo
        path  = [] # Armazena nodes já vizitados
        for item in vertices.keys():
            if vertices[item][0] == node and vertices[item][1] not in path:
                path.append(vertices[item][1])
                nodes.append([vertices[item][1],vertices[item][2]])
            elif vertices[item][1] == node and vertices[item][0] not in path:
                path.append(vertices[item][0])
                nodes.append([vertices[item][0],vertices[item][2]])

        print(nodes)


DijkstraAlgorithm('A')