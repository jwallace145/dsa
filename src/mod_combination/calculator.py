from dataclasses import dataclass
from typing import List


@dataclass
class ModCombinationCalculator:

    max_n: int
    mod: int  # needs to be prime according to Fermat's Little Theorem (i.e. 10^9 + 7)

    factorials: List[int] = None
    inverse_factorials: List[int] = None

    def __post_init__(self) -> None:
        self.factorials = ModCombinationCalculator.generate_factorials(
            self.max_n, self.mod
        )
        self.inverse_factorials = ModCombinationCalculator.generate_inverse_factorials(
            self.max_n, self.mod, self.factorials
        )

    def choose_combinations(self, k: int, n: int) -> int:
        if k < 0 or k > n:
            return 0
        return (
            self.factorials[n]
            * self.inverse_factorials[k]
            % self.mod
            * self.inverse_factorials[n - k]
            % self.mod
        )

    @staticmethod
    def generate_factorials(max_n: int, mod: int) -> List[int]:
        factorials = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            factorials[i] = (factorials[i - 1] * i) % mod
        return factorials

    @staticmethod
    def generate_inverse_factorials(
        max_n: int, mod: int, factorials: List[int]
    ) -> List[int]:
        inverse_factorials = [1] * (max_n + 1)
        inverse_factorials[max_n] = pow(factorials[max_n], mod - 2, mod)  # inverse modulus derived from Fermat's little theorem
        for i in range(max_n - 1, -1, -1):
            inverse_factorials[i] = (inverse_factorials[i + 1] * (i + 1)) % mod
        return inverse_factorials
