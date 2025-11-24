"""Stylish formatter for diff output."""


def format_value(value, depth):
    """Format values for output."""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        return format_dict(value, depth)
    else:
        return value


def format_dict(dictionary, depth):
    """Format a nested dictionary."""
    if not dictionary:
        return "{}"

    indent = "    " * depth
    lines = ["{"]

    for key, value in sorted(dictionary.items()):
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}    {key}: {formatted_value}")

    lines.append(f"{indent}}}")
    return "\n".join(lines)


def format_stylish(diff_tree, depth=0):
    """Format diff tree in stylish format."""
    lines = []
    indent = "    " * depth

    for node in sorted(diff_tree, key=lambda x: x["key"]):
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node["children"], depth + 1))
            lines.append(f"{indent}    }}")
        elif node_type == "added":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == "removed":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == "unchanged":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif node_type == "changed":
            old_value = format_value(node["old_value"], depth + 1)
            new_value = format_value(node["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")

    return "\n".join(lines)
