"""Build diff tree between two data structures."""


def build_diff(data1, data2):
    """
    Build a differences tree between two data structures.

    Each node has the form:
    {
        'type': 'added'|'removed'|'unchanged'|'changed'|'nested',
        'key': key,
        'value': value,           # for added, removed, unchanged
        'old_value': old_value,   # for changed
        'new_value': new_value,   # for changed
        'children': children      # for nested
    }
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {"key": key}

        if key not in data2:
            # Key removed
            node["type"] = "removed"
            node["value"] = data1[key]
        elif key not in data1:
            # Key added
            node["type"] = "added"
            node["value"] = data2[key]
        elif data1[key] == data2[key]:
            # No changes
            node["type"] = "unchanged"
            node["value"] = data1[key]
        else:
            # Value changed or nested structure
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                # Both are dictionaries - compare recursively
                node["type"] = "nested"
                node["children"] = build_diff(data1[key], data2[key])
            else:
                # Different values
                node["type"] = "changed"
                node["old_value"] = data1[key]
                node["new_value"] = data2[key]

        diff.append(node)

    return diff
