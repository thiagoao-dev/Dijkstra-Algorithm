__author__ = 'ThiagoAugustus'

import copy
import json

class DijkstraAlgorithm:

    file      = None
    graphCost = {}

    def __init__(self, node):
        self.file = self.readJson()
        self.mountTableCost(self.file['nodes'], node)
        self.dijkstra(self.file,node)

    # Lê o arquivo json
    def readJson(self):
        # Abre o arquivo conforme o caminho informado
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Testa o objeto
            assert isinstance(json_file, object)
            return json_file

    # Monta da table de custo dos nós
    def mountTableCost(self,nodes, node):
        for n in nodes:
            # Add custo zero para o nó inicial
            if n == node:
                self.graphCost[n] = 0
            else:
                self.graphCost[n] = -1

    def dijkstra(self, graph, node = None):
        nodes    = graph['nodes']
        vertices = graph['vertices']
        print(vertices)
        self.expandir(vertices, node)
        pass

    # Função que retorna as possíveis ações
    def expandir(self, vertices, node):
        # Cria caminhos
        nodes = [] # Armazena vetices e custo
        path  = [] # Armazena nodes já vizitados
        for item in vertices.keys():
            if vertices[item][0] == node and vertices[item][1] not in path:
                path.append(vertices[item][1])
                nodes.append([vertices[item][1],vertices[item][2]])
                print(vertices[item][2])
            elif vertices[item][1] == node and vertices[item][0] not in path:
                path.append(vertices[item][0])
                nodes.append([vertices[item][0],vertices[item][2]])

        print(nodes)


DijkstraAlgorithm('A')