import pytest
from src.main import divide

def test_divide_positive_numbers() -> None:
    """Test that divide returns the correct result when given two numbers."""
    assert divide(1, 2) == 0.5


def test_divide_negative_numbers() -> None:
    """
    Test that divide returns the correct result when given a positive and
    a negative number.
    """
    assert divide(5, -2) == -2.5
    assert divide(-2, 5) == -0.4

def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        divide('a', 5)
        divide(4, 'b')


# Use fixtures to reuse test data
# Use mock to isolate tests
