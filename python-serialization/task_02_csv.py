#!/usr/bin/python3
"""Convert CSV data to JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and saves it to data.json.
    Returns True on success, False on failure.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
