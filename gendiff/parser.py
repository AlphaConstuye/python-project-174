"""File parsing module for JSON and YAML formats."""

import json
import yaml


def load_file(file_path):
    """Load and parse a file according to its format."""
    if file_path.endswith('.json'):
        with open(file_path, encoding='utf-8') as file:
            return json.load(file)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path, encoding='utf-8') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Unsupported format: {file_path}")


def load_json(path):
    """Load JSON file (maintained for backward compatibility)."""
    return load_file(path)
