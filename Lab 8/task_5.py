def convert_date_format(date_str):
    """
    Converts a date from 'YYYY-MM-DD' format to 'DD-MM-YYYY' format.

    Args:
        date_str (str): Date string in 'YYYY-MM-DD' format.

    Returns:
        str: Date string in 'DD-MM-YYYY' format.
    """
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format.")
    return f"{parts[2]}-{parts[1]}-{parts[0]}"

# Example usage:
date_input = input("Enter date in 'YYYY-MM-DD' format: ")
try:
    converted_date = convert_date_format(date_input)
    print("Converted date:", converted_date)
except ValueError as e:
    print("Error:", e)