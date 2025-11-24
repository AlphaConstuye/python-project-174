import json
from gendiff.formatters.json import format_json


def test_format_json_flat():
    diff_tree = [
        {"type": "added", "key": "follow", "value": False},
        {"type": "removed", "key": "setting2", "value": 200},
        {
            "type": "changed",
            "key": "setting3",
            "old_value": True,
            "new_value": None,
        },
    ]

    result = format_json(diff_tree)
    # Parsear el JSON para verificar que es válido
    parsed_result = json.loads(result)

    # Verificar que contiene los elementos esperados
    assert len(parsed_result) == 3
    assert parsed_result[0]["type"] == "added"
    assert parsed_result[0]["key"] == "follow"
    assert parsed_result[0]["value"] is False


def test_format_json_nested():
    diff_tree = [
        {
            "type": "nested",
            "key": "common",
            "children": [
                {"type": "added", "key": "follow", "value": False},
                {
                    "type": "changed",
                    "key": "setting3",
                    "old_value": True,
                    "new_value": None,
                },
            ],
        }
    ]

    result = format_json(diff_tree)
    parsed_result = json.loads(result)

    assert len(parsed_result) == 1
    assert parsed_result[0]["type"] == "nested"
    assert parsed_result[0]["key"] == "common"
    assert len(parsed_result[0]["children"]) == 2


def test_format_json_complex_values():
    diff_tree = [
        {"type": "added", "key": "setting5", "value": {"key5": "value5"}},
        {
            "type": "changed",
            "key": "nest",
            "old_value": {"key": "value"},
            "new_value": "str",
        },
    ]

    result = format_json(diff_tree)
    parsed_result = json.loads(result)

    assert parsed_result[0]["type"] == "added"
    assert parsed_result[0]["value"] == {"key5": "value5"}
    assert parsed_result[1]["old_value"] == {"key": "value"}
