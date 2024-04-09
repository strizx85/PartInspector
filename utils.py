from datetime import datetime

def format_timestamp(timestamp=None, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Format a timestamp to a more readable form.

    :param timestamp: datetime or None, the timestamp to format. Uses current time if None.
    :param format_str: str, the format string.
    :return: str, the formatted timestamp.
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime(format_str)

def validate_part_number(part_number):
    """
    Validate a part number based on predefined rules.

    :param part_number: str, the part number to validate.
    :return: bool, True if valid, False otherwise.
    """
    # Example validation: part number should be alphanumeric and at least 4 characters long
    return part_number.isalnum() and len(part_number) >= 4

def convert_units(value, from_unit, to_unit):
    """
    Convert a measurement value from one unit to another.import os
from datetime import datetime

def format_timestamp(timestamp=None, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Format a timestamp to a more readable string format.
    
    :param timestamp: datetime or None. If None, uses the current time.
    :param format_str: str, format for the output timestamp string.
    :return: str, formatted timestamp.
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime(format_str)

def validate_part_number(part_number):
    """
    Validate a part number. Example: Must be alphanumeric and 4-10 characters long.
    
    :param part_number: str, the part number to validate.
    :return: bool, True if valid, False otherwise.
    """
    return part_number.isalnum() and 4 <= len(part_number) <= 10

def convert_units(value, from_unit, to_unit):
    """
    Convert a measurement value between specified units.
    
    :param value: float, the measurement value.
    :param from_unit: str, the unit of the measurement value.
    :param to_unit: str, the unit to convert the value to.
    :return: float, the converted value.
    :raises: ValueError, if the conversion is not supported.
    """
    conversion_factors = {
        ('inch', 'mm'): 25.4,
        ('mm', 'inch'): 1 / 25.4,
    }
    try:
        factor = conversion_factors[(from_unit, to_unit)]
        return value * factor
    except KeyError:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

def validate_document_path(doc_path):
    """
    Check if a document path is valid and the file exists.
    
    :param doc_path: str, the path to the document.
    :return: bool, True if the path is valid and the file exists, False otherwise.
    """
    return os.path.exists(doc_path) and os.path.isfile(doc_path)

# Example Usage
if __name__ == "__main__":
    print(format_timestamp())
    print(validate_part_number("1234ABCD"))
    try:
        print(convert_units(1, 'inch', 'mm'))
    except ValueError as e:
        print(e)
    print(validate_document_path("/path/to/document.pdf"))


    :param value: float, the measurement value to convert.
    :param from_unit: str, the unit to convert from.
    :param to_unit: str, the unit to convert to.
    :return: float, the converted value.
    """
    conversion_factor = {
        ('inch', 'mm'): 25.4,
        ('mm', 'inch'): 1/25.4
    }.get((from_unit, to_unit))

    if conversion_factor is None:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

    return value * conversion_factor

# Example usage:
if __name__ == "__main__":
    print(format_timestamp())
    print(validate_part_number("ABCD123"))
    try:
        print(f"1 inch to mm: {convert_units(1, 'inch', 'mm')}")
    except ValueError as e:
        print(e)
