import io
import json
import logging
import traceback

import fetch
from entities import *
from judge import stress
import UTIL


class Hacker:
    def __init__(self, metadata: dict, problems: list, hackable_submissions: list):
        self.metadata = metadata
        self.problems = problems
        self.hackable_submissions = hackable_submissions
        self.hack_log_file = f"{metadata['contest']}_hack.log"
        self.checked_file = f"{metadata['contest']}_checked.log"
        self.problem_mapper = {problem.code: problem for problem in problems}

    def publish_successful_hack(self, verdict: dict):
        with open(self.hack_log_file, "a") as file:
            for key, value in verdict.items():
                if key not in ['stdin', 'expected_output', 'defender_output']:
                    file.write(f'{key}: {value}\n')
                else:
                    file.write(f'{key}:\n{value}\n')

            file.write('*' * 128 + '\n')

    def publish_failed_hack(self, verdict: dict):
        with open(self.hack_log_file, "a") as file:
            for key, value in verdict.items():
                file.write(f'{key}: {value}\n')
                
            file.write('*' * 128 + '\n')

    def try_hack(self, problem: Problem, submission: Submission):
        logging.info(f"Trying to hack submission {submission.submission_id} ...")

        timeout = self.metadata["timeout"]
        stressor = stress.Stressor(problem, submission, timeout)
        stressor.prepare()
        verdict = stressor.test()
        if verdict['status'] == 'hacked':
            self.publish_successful_hack(verdict)
        else:
            self.publish_failed_hack(verdict)

        with open(self.checked_file, 'a') as file:
            file.write(f'{submission.submission_id}\n')

    def run(self):
        checked_submissions = set()
        try:
            with open(self.checked_file, 'r') as file:
                lines = file.readlines()
                lines = [line.strip() for line in lines]
                checked_submissions = set(lines)
        except:
            logging.error(traceback.format_exc())

        for submission in self.hackable_submissions:
            if submission['id'] in checked_submissions:
                continue
            try:
                submission = Submission(fetch.fetch_submission(submission))
                try:
                    problem = self.problem_mapper[submission.problem]
                except:
                    continue
                submission.set_limits(problem.time_limit, problem.memory_limit)
                submission.prepare()
                self.try_hack(problem, submission)
            except:
                logging.error(f"Exception when trying to hack {submission.submission_id}")
                logging.error(traceback.format_exc())

        for problem in self.problems:
            problem.executor.purge()