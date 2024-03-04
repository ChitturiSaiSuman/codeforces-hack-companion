import io
import json
import logging

import fetch
from entities import *
from judge import stress


class Hacker:
    def __init__(self, metadata: dict, problems: list, hackable_submissions: list):
        self.metadata = metadata
        self.problems = problems
        self.hackable_submissions = hackable_submissions
        self.hack_log_file = f"{metadata['contest']}_hack.log"
        self.problem_mapper = {problem.code: problem for problem in problems}

    def publish(self, verdict: dict):
        with open(self.hack_log_file, "a") as file:
            json.dump(verdict, file, indent=2)

    def try_hack(self, problem: Problem, submission: Submission):
        logging.info(f"Trying to hack submission {submission.submission_id} ...")
        
        timeout = self.metadata["timeout"]
        stressor = stress.Stressor(problem, submission, timeout)
        stressor.prepare()
        verdict = stressor.test()
        self.publish(verdict)

    def run(self):
        for submission in self.hackable_submissions:
            submission = Submission(fetch.fetch_submission(submission))
            try:
                problem = self.problem_mapper[submission.problem]
            except:
                continue
            submission.set_limits(problem.time_limit, problem.memory_limit)
            submission.prepare()
            self.try_hack(problem, submission)
