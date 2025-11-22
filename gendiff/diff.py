from gendiff.parser import load_file


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def generate_diff(file1, file2):
    data1 = load_file(file1)
    data2 = load_file(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    lines = ["{"]

    for key in keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")

    lines.append("}")

    return "\n".join(lines)
