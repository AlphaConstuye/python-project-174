import json


def format_json(diff_tree):
    """
    Formatea el árbol de diferencias en formato JSON
    """
    return json.dumps(diff_tree, indent=2)
