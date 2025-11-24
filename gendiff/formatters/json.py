"""JSON formatter for diff output."""

import json


def format_json(diff_tree):
    """Format diff tree in JSON format."""
    return json.dumps(diff_tree, indent=2)
