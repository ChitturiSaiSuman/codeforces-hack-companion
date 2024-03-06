import io
import random
from abc import ABC, abstractmethod


class Generator(ABC):
    @classmethod
    def get_generator(cls, generator: str):
        for subclass_name, subclass in globals().items():
            if isinstance(subclass, type) and issubclass(subclass, cls) and subclass.__name__ == generator:
                return subclass

        raise ValueError(f"No Generator found with the name {generator}!")

    def __init__(self):
        self.buffer = io.StringIO()
        self.stdin = None
        self.stdout = None
        self.stdexpout = None

    def print(self, *args, **kwargs):
        print(*args, **kwargs, file=self.buffer)

    def clear(self):
        self.buffer.seek(0)
        self.buffer.truncate(0)

    def __process(self, contents: str) -> list:
        contents = contents.strip().splitlines()
        contents = list(map(lambda x: x.strip(), contents))
        return contents[::-1]

    def sanitize(self):
        self.stdin = self.__process(self.stdin)
        self.stdout = self.__process(self.stdout)
        self.stdexpout = self.__process(self.stdexpout)

    @abstractmethod
    def generate(self, seed: int) -> str:
        pass


class AlphaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1000, 5000)
        self.print(T)

        for t in range(T):
            N = random.randint(2, 20)
            self.print(N)
            arr = [random.randint(0, N - 1) for i in range(N)]
            self.print(*arr)


        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        # return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        def find_mex(arr: list) -> int:
            arr = set(arr)
            i = 0
            while i in arr:
                i += 1
            return i

        T = int(read(stdin)) # Number of test cases
        for t in range(T):
            N = int(read(stdin))
            arr = list(map(int, read(stdin).split()))
            possible = int(read(stdexpout))
            outcome = int(read(stdout))
            if possible == -1:
                if outcome != -1:
                    return False
            else:
                if outcome == 1:
                    return False
                
                for i in range(possible):
                    pairs = read(stdexpout)
                
                pairs = []
                for i in range(outcome):
                    start, end = map(int, read(stdout).split())
                    pairs.append((start, end))
                
                for i in range(outcome - 1):
                    if pairs[i + 1][0] != pairs[i][1] + 1:
                        return False
                    
                if pairs[0][0] != 1 or pairs[-1][1] != N:
                    return False
                
                mexes = set()
                for pair in pairs:
                    mexes.add(find_mex(arr[pair[0] - 1:pair[1]]))

                if len(mexes) > 1:
                    return False
                
        return True
                    


class BetaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 10**4)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class GammaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class DeltaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class EpsilonGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class ZetaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class EtaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class ThetaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class LambdaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases


class SigmaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(1, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 10**9)
            self.print(N)

        # ################################################################
        """
        Generator ends
        """
        self.stdin = self.buffer.getvalue()
        self.clear()
        return self.stdin

    def validate(self, expected_output: str, defender_output: str):
        self.stdexpout = expected_output
        self.stdout = defender_output
        self.sanitize()

        def read(file: list) -> str:
            return file.pop()

        stdin = self.stdin
        stdout = self.stdout
        stdexpout = self.stdexpout

        return stdout == stdexpout

        # Comment above and Write your custom judge here
        # Example:

        # T = int(read(stdin)) # Number of test cases
