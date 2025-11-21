from gendiff.parser import load_json


def generate_diff(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    lines = ["{"]

    for key in keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {data1[key]}")
        else:
            lines.append(f"  - {key}: {data1[key]}")
            lines.append(f"  + {key}: {data2[key]}")

    lines.append("}")

    return "\n".join(lines)

