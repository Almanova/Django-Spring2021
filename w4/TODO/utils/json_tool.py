import json


def read_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return list()
