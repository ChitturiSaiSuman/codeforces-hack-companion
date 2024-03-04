import logging
import time

from entities import *
from judge.remo import Remo


class Stressor:
    def __init__(self, problem: Problem, submission: Submission, timeout: int):
        self.problem = problem
        self.submission = submission
        self.timeout = timeout

    def prepare(self):
        self.problem.prepare()
        self.submission.prepare()
        self.generator = self.problem.generator

    def test(self):
        seed = 1
        start_time = time.time()

        while time.time() - start_time < self.timeout:
            stdin = self.generator.generate(seed)
            expected_outcome = self.problem.executor.run(stdin)
            defender_outcome = self.submission.executor.run(stdin)

            if "error" in [expected_outcome["status"], defender_outcome["status"]]:
                logging.error(expected_outcome.get("message", None))
                logging.error(defender_outcome.get("message", None))
                return
            else:
                expected_output = expected_outcome["stdout"]
                defender_output = defender_outcome["stdout"]
                result = self.generator.validate(expected_output, defender_output)

                if not result:
                    return {
                        "status": "hacked",
                        "seed": seed,
                        "generator": self.generator.__class__.__name__,
                        "submission_id": self.submission.submission_id,
                        "problem": self.submission.problem
                    }
            seed += 1

        return {
            "status": "failed hack attempt",
            "generator": self.generator.__class__.__name__,
            "submission_id": self.submission.submission_id,
            "problem": self.submission.problem
        }
