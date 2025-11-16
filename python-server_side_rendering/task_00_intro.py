#!/usr/bin/python3
"""
Module for generating personalized invitation files from a template.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template with placeholders.
    
    Args:
        template (str): A string containing the invitation template with placeholders
        attendees (list): A list of dictionaries containing attendee information
    
    The function will:
    - Validate input types
    - Handle empty inputs
    - Replace placeholders with actual values
    - Generate output files named output_X.txt
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check if attendees list contains dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        personalized_invitation = template
        
        # Replace placeholders with actual values or "N/A" if missing
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Check if value is None or empty
            if value is None or value == "":
                value = "N/A"
            personalized_invitation = personalized_invitation.replace(
                "{" + placeholder + "}", str(value)
            )
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_invitation)
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")
