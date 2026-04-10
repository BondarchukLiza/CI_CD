import pytest
from writer import write_result


def test_write_result(tmp_path):
    file = tmp_path / "output.txt"
    data = [("hello", 2), ("world", 1)]

    write_result(file, data)

    content = file.read_text()
    assert content == "hello-2\nworld-1\n"