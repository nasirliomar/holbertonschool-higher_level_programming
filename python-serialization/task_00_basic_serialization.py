#!/usr/bin/python3
"""Basic JSON serialization and deserialization"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from a file and return it as a dictionary."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
