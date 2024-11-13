#task 1
import re

def solve_codewars_challenges(phone_number, bus_stops):
    # Challenge 1: Validate phone number
    is_valid_phone = bool(re.fullmatch(r"\(\d{3}\) \d{3}-\d{4}", phone_number))
    
    # Challenge 2: Calculate number of people left on the bus
    people_left = sum(on - off for on, off in bus_stops)
    
    # Return results as a dictionary
    return {
        "valid_phone_number": is_valid_phone,
        "people_left_on_bus": people_left
    }
print(valid_phone_number("(123) 456-7890"))  # True
print(valid_phone_number("123-456-7890"))    # False

#task 2
import re

def solve_codewars_challenges(phone_number, bus_stops):
    # Challenge 1: Validate phone number
    is_valid_phone = bool(re.fullmatch(r"\(\d{3}\) \d{3}-\d{4}", phone_number))
    
    # Challenge 2: Calculate number of people left on the bus
    people_left = sum(on - off for on, off in bus_stops)
    
    # Return results as a dictionary
    return {
        "valid_phone_number": is_valid_phone,
        "people_left_on_bus": people_left
    }

result = solve_codewars_challenges("(123) 456-7890", [(10, 0), (3, 5), (5, 8)])
print(result)  # {'valid_phone_number': True, 'people_left_on_bus': 5}

result = solve_codewars_challenges("123-456-7890", [(3, 0), (9, 1), (4, 10), (12, 2)])
print(result)  # {'valid_phone_number': False, 'people_left_on_bus': 15}
