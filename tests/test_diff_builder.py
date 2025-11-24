from gendiff.diff_builder import build_diff


def test_build_diff_flat():
    data1 = {"a": 1, "b": 2}
    data2 = {"a": 1, "c": 3}

    result = build_diff(data1, data2)

    expected_types = ["unchanged", "removed", "added"]
    result_types = [node["type"] for node in result]

    assert sorted(result_types) == sorted(expected_types)


def test_build_diff_nested():
    data1 = {"a": {"b": 1}}
    data2 = {"a": {"b": 2}}

    result = build_diff(data1, data2)

    assert result[0]["type"] == "nested"
    assert "children" in result[0]
    assert result[0]["children"][0]["type"] == "changed"
