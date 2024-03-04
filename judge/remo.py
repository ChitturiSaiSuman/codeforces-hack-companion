#!/usr/bin/python3

import asyncio
import collections
import inspect
import json
import logging
import traceback

from config import Constants
from judge.executor import Executor
from judge.job import Job


class Remo:
    @classmethod
    def __is_executor(cls, member) -> bool:
        return inspect.isclass(member[1]) and member[1].__module__ == Executor.__module__

    @classmethod
    def __list_executors(cls) -> list:
        return list(filter(cls.__is_executor, inspect.getmembers(Executor)))

    @classmethod
    def __load(cls) -> dict:
        cls.__executors = dict(cls.__list_executors())

    def __init__(self, args: collections.defaultdict):
        Remo.__load()

        print(args['lang'])

        args['lang'] = args['lang']['MAPPING']

        self.lang = args['lang']
        self.args = args
        
        # print(Remo.__executors)
        # print(self.lang)

        try:
            self.executor = Remo.__executors[self.lang]()
            prep_response = self.executor.prepare(self.args)

            if prep_response['status'] == 'error':
                raise Exception(prep_response['message'])
            
        except Exception as e:
            raise

    def run(self, stdin: str) -> collections.defaultdict:
        response = collections.defaultdict()
        try:

            run_response = self.executor.run(stdin)
            return run_response
        
        except Exception as e:
            response['status'] = 'error'
            response['message'] = traceback.format_exc()
            
        return response