import pytest
from reader import read_file


@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello world")
    return file


def test_read_file(sample_file):
    content = read_file(sample_file)
    assert content == "hello world"