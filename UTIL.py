import json
from config import Constants

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


def get_langauge(lang: str) -> dict:
    allowed_languages = Constants.setup['ALLOWED_LANGUAGES']
    for language in allowed_languages:
        if language['LANGUAGE'] == lang:
            return language
        
    return {}