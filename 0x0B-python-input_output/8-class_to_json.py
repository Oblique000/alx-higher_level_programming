#!/usr/bin/python3
"""8-class_to_json module"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.
    Args:
        obj: is an instance of a Class.
    Return:
        dict: returns the dictionary description.
    """
    if hasattr(obj, '__dict__'):
        return {key: value for key, value in obj.__dict__.items() if is_serializable(value)}
    return {}


def is_serializable(value):
    """Check if the value is serializable."""
    try:
        json.dumps(value)
        return True
    except (TypeError, OverflowError):
        return False
