def cm_to_inches(cm):
    inches = cm / 2.54
    return round(inches, 2)

# Example usage
cm_value = 10
inches_value = cm_to_inches(cm_value)
print(f"{cm_value} cm = {inches_value} inches")