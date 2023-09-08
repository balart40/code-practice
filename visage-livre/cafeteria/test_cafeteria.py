import pytest
from solution_cafeteria import Solution

@pytest.mark.parametrize(
    "N, K, M, S, want",
    (
            (10, 1, 2, [2,6], 3),
    ),
)
def test_cafeteria(N, K, M, S, want):
    solution = Solution()
    got = solution.getMaxAdditionalDinersCount(N, K, M, S)
    assert got == want