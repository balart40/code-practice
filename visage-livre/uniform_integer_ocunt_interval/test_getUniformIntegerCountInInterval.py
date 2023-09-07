import pytest
from solution_uniform_integer_ocunt_interval import Solution

@pytest.mark.parametrize(
    "A, B, want",
    (
            (75, 300, 5),
    ),
)
def test_getUniformIntegerCountInInterval(A, B, want):
    solution = Solution()
    got = solution.getUniformIntegerCountInInterval(A, B)
    assert got == want