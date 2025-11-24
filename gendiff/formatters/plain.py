def format_value(value):
    """Formatea valores para el output plain"""
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return value


def format_plain(diff_tree, path=''):
    """
    Formatea el árbol de diferencias en formato plain
    """
    lines = []
    
    for node in sorted(diff_tree, key=lambda x: x['key']):
        key = node['key']
        node_type = node['type']
        current_path = f"{path}.{key}" if path else key

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        
        elif node_type == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {old_value} to {new_value}")

    return "\n".join([line for line in lines if line])
