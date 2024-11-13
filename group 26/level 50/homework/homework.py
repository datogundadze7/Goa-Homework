def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    # Define time units in seconds
    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]
    
    # Calculate each unit and build the list of non-zero components
    result = []
    for name, unit_seconds in units:
        quantity = seconds // unit_seconds
        if quantity:
            result.append(f"{quantity} {name}{'s' if quantity > 1 else ''}")
        seconds %= unit_seconds
    
    # Join with commas and "and" for readability
    if len(result) == 1:
        return result[0]
    return ", ".join(result[:-1]) + " and " + result[-1]

print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds"
print(format_duration(62))    # "1 minute and 2 seconds"
print(format_duration(0))     # "now"
