#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""
import sys
import os

# Import functions from previous files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if file exists to decide whether to load or start fresh
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
