import io
import random

import fetch
from judge.remo import Remo
from judge.generator import Generator


class Problem:
    def __init__(self, args: dict):
        for key, value in args.items():
            setattr(self, key, value)
        # self.code = args['code']
        # self.name = args['name']
        # self.time_limit = args['time_limit']
        # self.memory_limit = args['memory_limit']
        # self.generator = args['generator']
        # self.reference_submission = args['reference_submission']

    def prepare(self):
        if hasattr(self, 'executor'):
            return
        
        self.reference_submission = Submission(
            fetch.fetch_reference_submission(self.reference_submission)
        )
        args = {
            "lang": self.reference_submission.language,
            "source": self.reference_submission.source,
            "time_limit": int(self.time_limit),
            "memory_limit": int(self.memory_limit) * 1024,  # Convert to KB
            "source_file_name": f"{self.reference_submission.submission_id}{self.reference_submission.language['EXTENSION']}",
            "path": "/tmp/",
            "executable": f"{self.reference_submission.submission_id}_exe"
        }
        # print(args)
        self.executor = Remo(args)

        # Instantiate Generator
        self.generator = Generator.get_generator(self.generator)()


class Submission:
    def __init__(self, args: dict):
        for key, value in args.items():
            setattr(self, key, value)
        # print(args)
        # self.submission_id = args["submission_id"]
        # self.problem = args["problem"]
        # self.contest_id = args["contest_id"]
        # self.owner = args["owner"]
        # self.language = args["language"]
        # self.source = args["source"]
        # self.verdict = args["verdict"]
            
    def set_limits(self, time_limit: int, memory_limit: int):
        self.time_limit = int(time_limit) * self.language['MULTIPLIER']
        self.memory_limit = int(memory_limit)
            
    def prepare(self):
        if hasattr(self, 'executor'):
            return
        
        args = {
            "lang": self.language,
            "source": self.source,
            "time_limit": self.time_limit,
            "memory_limit": int(self.memory_limit) * 1024,
            "source_file_name": f"{self.submission_id}{self.language['EXTENSION']}",
            "path": f"/tmp/",
            "executable": f"{self.submission_id}_exe"
        }
        # print(args)
        self.executor = Remo(args)