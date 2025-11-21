import os
from gendiff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "fixtures")

def read_fixture(filename):
    path = os.path.join(FIXTURES_PATH, filename)
    with open(path, 'r') as f:
        return f.read().strip()

def test_flat_json():
    file1 = os.path.join(FIXTURES_PATH, "file1.json")
    file2 = os.path.join(FIXTURES_PATH, "file2.json")
    expected = read_fixture("expected_flat.txt")

    result = generate_diff(file1, file2)
    assert result.strip() == expected

