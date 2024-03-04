import json

from entities import *

def get_metadata() -> dict:
    metadata_file = 'metadata.json'
    with open(metadata_file, 'r') as file:
        metadata = json.load(file)
        return metadata
    

def prepare(metadata: dict) -> list:
    problems = list(map(Problem, metadata['problems']))
    for problem in problems:
        problem.prepare()

    return problems