def build_diff(data1, data2):
    """
    Construye un árbol de diferencias entre dos estructuras de datos.
    Cada nodo tiene la forma:
    {
        'type': 'added'|'removed'|'unchanged'|'changed'|'nested',
        'key': key,
        'value': value,           # para added, removed, unchanged
        'old_value': old_value,   # para changed
        'new_value': new_value,   # para changed
        'children': children      # para nested
    }
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {'key': key}

        if key not in data2:
            # Clave eliminada
            node['type'] = 'removed'
            node['value'] = data1[key]
        elif key not in data1:
            # Clave agregada
            node['type'] = 'added'
            node['value'] = data2[key]
        elif data1[key] == data2[key]:
            # Sin cambios
            node['type'] = 'unchanged'
            node['value'] = data1[key]
        else:
            # Valor cambiado o estructura anidada
            if (isinstance(data1[key], dict) and
                    isinstance(data2[key], dict)):
                # Ambos son diccionarios - comparar recursivamente
                node['type'] = 'nested'
                node['children'] = build_diff(data1[key], data2[key])
            else:
                # Valores diferentes
                node['type'] = 'changed'
                node['old_value'] = data1[key]
                node['new_value'] = data2[key]

        diff.append(node)

    return diff
