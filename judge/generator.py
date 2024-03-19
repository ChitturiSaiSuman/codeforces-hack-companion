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

        T = random.randint(10**4, 10**4)
        self.print(T)

        for test in range(T):
            a = random.randint(0, 10**9)
            b = random.randint(0, 10**9)
            c = random.randint(0, 10**9)
            self.print(a, b, c)


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


class BetaGenerator(Generator):
    def generate(self, seed: int) -> str:
        random.seed(seed)
        """
        Your Generator goes here
        """
        # ################################################################

        T = random.randint(10**4, 10**4)
        self.print(T)

        for t in range(T):
            a, b, m = [random.randint(1, 10**18) for i in range(3)]
            self.print(a, b, m)

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

        T = random.randint(100, 100)
        self.print(T)

        for t in range(T):
            N = random.randint(3, 10**3)
            self.print(N)
            bits = ''.join(
                [
                    str(random.randint(0, 1)) for i in range(N)
                ]
            )
            self.print(bits)

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

        T = random.randint(100, 1000)
        self.print(T)

        for test in range(T):
            n = random.randint(1, 2 * 10**4)
            m = random.randint(1, n)
            self.print(n, m)
            a = [random.randint(1, 10**9) for i in range(n)]
            b = [random.randint(1, 10**9) for i in range(n)]
            self.print(*a)
            self.print(*b)

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

        T = random.randint(100, 1000)
        self.print(T)

        for t in range(T):
            N = random.randint(1, 5 * 10**4)
            self.print(N)
            arr = [random.randint(1, 10**9) for i in range(N)]
            self.print(arr)
            perm = [i for i in range(1, N + 1)]
            random.shuffle(perm)
            self.print(*perm)

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

        for a, b in zip(stdout, stdexpout):
            if list(map(int, a.split())) != list(map(int, b.split())):
                return False

        return True

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
