import copy
import json

__author__ = 'ThiagoAugustus'

# Lê o arquivo json
def readJson():
    # Abre o arquivo conforme o caminho informado
    with open("grafod.json") as json_file:
        json_file = json.load(json_file)
        # Testa o objeto
        assert isinstance(json_file, object)
        return json_file


def dijkstra(graph, node = None):
    nodes    = graph['nodes']
    vertices = graph['vertices']
    print(vertices)
    expandir(vertices, node)
    pass

# Função que retorna as possíveis ações
def expandir(vertices, node):
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
    '''
    # Cria uma cópia do grafo para manipulação
    gCopy = copy.deepcopy(vertices)
    # Varre todos os nós do grafo
    for n,v in gCopy.items():
        # Verifica se em cada tupla há uma ligação com o nó
        for i in v:
            # Caso o nó exista na tupla
            if int(node) == i:
                # Remove o nó atual
                v.remove(int(node))
                # Adciona o nó que faz link na lista
                nodes.append(v[0])
    # Organiza os nós por ordem númerica
    nodes.sort()
    '''
    return nodes

grafo = readJson()
dijkstra(grafo,'H')