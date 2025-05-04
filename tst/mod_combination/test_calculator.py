from src.mod_combination.calculator import ModCombinationCalculator


def test_create_factorials() -> None:
    assert [1] == ModCombinationCalculator.generate_factorials(max_n=0, mod=10**9 + 7)
    assert [1, 1] == ModCombinationCalculator.generate_factorials(
        max_n=1, mod=10**9 + 7
    )
    assert [1, 1, 2] == ModCombinationCalculator.generate_factorials(
        max_n=2, mod=10**9 + 7
    )
    assert [1, 1, 2, 6] == ModCombinationCalculator.generate_factorials(
        max_n=3, mod=10**9 + 7
    )
    assert [1, 1, 2, 6, 24] == ModCombinationCalculator.generate_factorials(
        max_n=4, mod=10**9 + 7
    )
    assert [1, 1, 2, 6, 24, 120] == ModCombinationCalculator.generate_factorials(
        max_n=5, mod=10**9 + 7
    )


def test_create_inverse_factorials() -> None:
    assert [1] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=0, mod=10**9 + 7, factorials=[1]
    )
    assert [1, 1] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=1, mod=10**9 + 7, factorials=[1, 1]
    )
    assert [1, 1, 500000004] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=2, mod=10**9 + 7, factorials=[1, 1, 2]
    )
    assert [
        1,
        1,
        500000004,
        166666668,
    ] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=3, mod=10**9 + 7, factorials=[1, 1, 2, 6]
    )
    assert [
        1,
        1,
        500000004,
        166666668,
        41666667,
    ] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=4, mod=10**9 + 7, factorials=[1, 1, 2, 6, 24]
    )
    assert [
        1,
        1,
        500000004,
        166666668,
        41666667,
        808333339,
    ] == ModCombinationCalculator.generate_inverse_factorials(
        max_n=5, mod=10**9 + 7, factorials=[1, 1, 2, 6, 24, 120]
    )
