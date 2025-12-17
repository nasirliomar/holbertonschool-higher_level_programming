#!/usr/bin/python3
"""
task_00_intro.py

Generate personalized invitation files from a template and a list of attendees.
"""

def generate_invitations(template, attendees):
    # ---- Type checks ----
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type: attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    for i, item in enumerate(attendees):
        if not isinstance(item, dict):
            print(
                "Invalid input type: attendees must be a list of dictionaries, "
                f"but item at index {i} is {type(item).__name__}."
            )
            return

    # ---- Empty checks ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # ---- Generate output files ----
    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None or value == "":
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
        except OSError as err:
            print(f"Error writing {filename}: {err}")
            return
