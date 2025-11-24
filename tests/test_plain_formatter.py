import pytest
from gendiff.formatters.plain import format_plain


def test_format_plain_flat():
    diff_tree = [
        {'type': 'added', 'key': 'follow', 'value': False},
        {'type': 'removed', 'key': 'setting2', 'value': 200},
        {'type': 'changed', 'key': 'setting3', 'old_value': True, 'new_value': None}
    ]
    
    result = format_plain(diff_tree)
    expected = "Property 'follow' was added with value: false\nProperty 'setting2' was removed\nProperty 'setting3' was updated. From true to null"
    
    assert result == expected


def test_format_plain_nested():
    diff_tree = [
        {
            'type': 'nested', 
            'key': 'common', 
            'children': [
                {'type': 'added', 'key': 'follow', 'value': False},
                {'type': 'changed', 'key': 'setting3', 'old_value': True, 'new_value': None}
            ]
        }
    ]
    
    result = format_plain(diff_tree)
    expected = "Property 'common.follow' was added with value: false\nProperty 'common.setting3' was updated. From true to null"
    
    assert result == expected


def test_format_plain_complex_values():
    diff_tree = [
        {'type': 'added', 'key': 'setting5', 'value': {'key5': 'value5'}},
        {'type': 'changed', 'key': 'nest', 'old_value': {'key': 'value'}, 'new_value': 'str'}
    ]
    
    result = format_plain(diff_tree)
    # 'nest' viene alfabéticamente antes que 'setting5'
    expected = "Property 'nest' was updated. From [complex value] to 'str'\nProperty 'setting5' was added with value: [complex value]"
    
    assert result == expected
