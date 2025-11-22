import json
import yaml


def load_file(file_path):
    """
    Carga y parsea un archivo según su formato (JSON o YAML)
    """
    if file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path) as f:
            return yaml.safe_load(f)
    else:
        raise ValueError(f"Formato no soportado: {file_path}")


# Mantén la función load_json para compatibilidad con código existente
def load_json(path):
    return load_file(path)
