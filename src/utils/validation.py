# src/utils/validation.py

import jsonschema
from jsonschema import Draft7Validator

assignment_schema = {
    "type": "object",
    "properties": {
        "Requesting Party": {
            "type": "object",
            "properties": {
                "Insurance Company": {"type": ["string", "null"]},
                "Handler": {"type": ["string", "null"]},
                "Carrier Claim Number": {"type": ["string", "null"]},
            },
        },
        "Insured Information": {
            "type": "object",
            "properties": {
                "Name": {"type": ["string", "null"]},
                "Contact #": {"type": ["string", "null"]},
                "Loss Address": {"type": ["string", "null"]},
                "Public Adjuster": {"type": ["string", "null"]},
                "Owner or Tenant": {"type": ["string", "null"]},
            },
        },
        "Adjuster Information": {
            "type": "object",
            "properties": {
                "Adjuster Name": {"type": ["string", "null"]},
                "Adjuster Phone Number": {"type": ["string", "null"]},
                "Adjuster Email": {"type": ["string", "null"]},
                "Job Title": {"type": ["string", "null"]},
                "Address": {"type": ["string", "null"]},
                "Policy #": {"type": ["string", "null"]},
            },
        },
        "Assignment Information": {
            "type": "object",
            "properties": {
                "Date of Loss/Occurrence": {"type": ["string", "null"]},
                "Cause of loss": {"type": ["string", "null"]},
                "Facts of Loss": {"type": ["string", "null"]},
                "Loss Description": {"type": ["string", "null"]},
                "Residence Occupied During Loss": {"type": ["string", "boolean", "null"]},
                "Was Someone home at time of damage": {"type": ["string", "boolean", "null"]},
                "Repair or Mitigation Progress": {"type": ["string", "null"]},
                "Type": {"type": ["string", "null"]},
                "Inspection type": {"type": ["string", "null"]},
            },
        },
        "Assignment Type": {
            "type": "object",
            "properties": {
                "Wind": {"type": ["boolean", "null"]},
                "Structural": {"type": ["boolean", "null"]},
                "Hail": {"type": ["boolean", "null"]},
                "Foundation": {"type": ["boolean", "null"]},
                "Other": {
                    "type": "object",
                    "properties": {
                        "Checked": {"type": ["boolean", "null"]},
                        "Details": {"type": ["string", "null"]},
                    },
                },
            },
        },
        "Additional details/Special Instructions": {"type": ["string", "null"]},
        "Attachment(s)": {
            "type": "array",
            "items": {"type": "string"},
        },
        "Entities": {
            "type": "object",
            "additionalProperties": {"type": "array", "items": {"type": "string"}},
        },
    },
}

def validate_json(parsed_data):
    validator = Draft7Validator(assignment_schema)
    errors = sorted(validator.iter_errors(parsed_data), key=lambda e: e.path)
    
    if errors:
        error_messages = [f"{'.'.join(map(str, error.path))}: {error.message}" for error in errors]
        return False, "\n".join(error_messages)
    return True, ""