from gendiff.parser import load_file
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def generate_diff(file1, file2, format_name='stylish'):
    """
    Genera la diferencia entre dos archivos
    """
    data1 = load_file(file1)
    data2 = load_file(file2)

    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return "{\n" + format_stylish(diff_tree) + "\n}"
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f"Formato no soportado: {format_name}")
