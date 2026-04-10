import pytest
from processor import get_top_words


@pytest.mark.parametrize("text,expected", [
    ("hello hello world", [("hello", 2), ("world", 1)]),
    ("a a a b b c", [("a", 3), ("b", 2), ("c", 1)])
])
def test_get_top_words(text, expected):
    result = get_top_words(text, top_n=3)
    assert result == expected