import pytest
from solution_stack_stabilization import Solution

@pytest.mark.parametrize(
    "N, R, want",
    (
            (5, [2, 5, 3, 6, 5], 3),
    ),
)
def test_getMinimumDeflatedDiscCount(N, R, want):
    solution = Solution()
    got = solution.getMinimumDeflatedDiscCount(N, R)
    assert got == want