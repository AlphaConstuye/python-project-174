from gendiff.formatters.stylish import format_stylish


def test_format_stylish_flat():
    diff_tree = [
        {"type": "unchanged", "key": "a", "value": 1},
        {"type": "removed", "key": "b", "value": 2},
        {"type": "added", "key": "c", "value": 3},
    ]

    result = format_stylish(diff_tree)
    expected = "    a: 1\n  - b: 2\n  + c: 3"

    assert result == expected


def test_format_stylish_nested():
    diff_tree = [
        {
            "type": "nested",
            "key": "a",
            "children": [
                {"type": "changed", "key": "b", "old_value": 1, "new_value": 2}
            ],
        }
    ]

    result = format_stylish(diff_tree)
    # Usar la indentación real que produce el formateador
    expected = "    a: {\n      - b: 1\n      + b: 2\n    }"

    assert result == expected


def test_format_stylish_dict_value():
    diff_tree = [{"type": "added", "key": "a", "value": {"b": 1, "c": 2}}]

    result = format_stylish(diff_tree)
    # Verifica que los diccionarios anidados se formateen correctamente
    assert "b: 1" in result
    assert "c: 2" in result
    assert "{" in result
    assert "}" in result
