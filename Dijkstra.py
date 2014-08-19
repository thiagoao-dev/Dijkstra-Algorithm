__author__ = 'ThiagoAugustus'

import json

# Lê o arquivo json
def readJson():
    # Abre o arquivo conforme o caminho informado
    with open(input("grafod.json")) as json_file:
        json_file = json.load(json_file)
        # Testa o objeto
        assert isinstance(json_file, object)
        return json_file

grafo = readJson()

print(grafo, 'ok')