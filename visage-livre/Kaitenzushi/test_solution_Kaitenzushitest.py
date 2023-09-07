import pytest
from solution_Kaitenzushi import Solution


@pytest.mark.parametrize(
    "N, D, K, want",
    (
            (6, [1, 2, 3, 3, 2, 1], 1, 5),
    ),
)
def test_getMaximumEatenDishCount(N, D, K, want):
    solution = Solution()
    got = solution.getMaximumEatenDishCount(N, D, K)
    assert got == want

#pytest.main()