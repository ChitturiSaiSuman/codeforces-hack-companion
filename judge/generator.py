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

        T = random.randint(1, 10**3)
        self.print(T)

        for test in range(T):
            N = random.randint(1, 10**2)
            M = random.randint(1, 10**2)
            K = random.randint(1, 10**2)
            self.print(N, M, K)

            arr = []
            s = set()
            while len(arr) < N:
                ele = random.randint(1, 2 * 10**9)
                while ele in s:
                    ele = random.randint(1, 2 * 10**9)
                arr.append(ele)
                s.add(ele)

            B = [random.randint(1, 10**9) for i in range(M)]
            C = [random.randint(1, 10**9) for i in range(K)]

            self.print(*arr)
            self.print(*B)
            self.print(*C)


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

        T = read()
                    


class BetaGenerator(Generator):
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
