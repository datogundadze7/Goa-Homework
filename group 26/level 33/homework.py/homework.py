def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("month", 30 * 24 * 60 * 60),
        ("week", 7 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]
    
    parts = []
    
    for unit_name, unit_seconds in time_units:
        if seconds >= unit_seconds:
            value = seconds // unit_seconds
            seconds %= unit_seconds
            parts.append(f"{value} {unit_name}{'s' if value > 1 else ''}")
    
    if len(parts) == 1:
        return parts[0]
    
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]

# Examples
print(format_duration(62))    # Output: "1 minute and 2 seconds"
print(format_duration(3662))  # Output: "1 hour, 1 minute and 2 seconds"
print(format_duration(0))     # Output: "now"

#task 2
# 1. გაწვდოს ნულის მიერ გაწვდვა
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Ошибка: არ შეგიძლიათ გაწვდოთ ნულზე."
    except TypeError:
        return "Ошибка: არასწორი ტიპი."
    else:
        return f"შედეგი არის {result:.2f}"

# მაგალითები
print("გაწვდოს ნულის მიერ გაწვდვა მაგალითები:")
print(safe_divide(10, 2))  # Output: შედეგი არის 5.00
print(safe_divide(10, 0))  # Output: Ошибка: არ შეგიძლიათ გაწვდოთ ნულზე.
print(safe_divide(10, 'a'))  # Output: Ошибка: არასწორი ტიპი.
print()

# 2. ფაილის წაკითხვა
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Ошибка: ფაილი ვერ მოიძებნა."
    except IOError:
        return "Ошибка: IO შეცდომა მოხდა."
    else:
        return content

# მაგალითები
print("ფაილის წაკითხვა მაგალითები:")
print(read_file('existing_file.txt'))  # Output: (ფაილის შინაარსი ან შესაბამისი შეცდომა)
print(read_file('nonexistent_file.txt'))  # Output: Ошибка: ფაილი ვერ მოიძებნა.
print()

# 3. სიის ინდექსი არასწორად
def get_element_from_list(lst, index):
    try:
        element = lst[index]
    except IndexError:
        return "Ошибка: ინდექსი არასწორია."
    except TypeError:
        return "Ошибка: სია არასწორად არის ფორმატირებული."
    else:
        return f"ელემენტი ინდექსზე {index} არის {element}"

# მაგალითები
print("სიის ინდექსი არასწორად მაგალითები:")
print(get_element_from_list([1, 2, 3], 1))  # Output: ელემენტი ინდექსზე 1 არის 2
print(get_element_from_list([1, 2, 3], 5))  # Output: Ошибка: ინდექსი არასწორია.
print(get_element_from_list('not_a_list', 1))  # Output: Ошибка: სია არასწორად არის ფორმატირებული.
print()

# 4. მნიშვნელობის გარდაქმნა
def convert_to_integer(value):
    try:
        integer_value = int(value)
    except ValueError:
        return "Ошибка: ვერ გარდაქმნება მნიშვნელობა integer-ში."
    except TypeError:
        return "Ошибка: გადაცემული მნიშვნელობა არ არის სწორი."
    else:
        return f"integer მნიშვნელობა არის {integer_value}"

# მაგალითები
print("მნიშვნელობის გარდაქმნა მაგალითები:")
print(convert_to_integer('123'))  # Output: integer მნიშვნელობა არის 123
print(convert_to_integer('abc'))  # Output: Ошибка: ვერ გარდაქმნება მნიშვნელობა integer-ში.
print(convert_to_integer(12.34))  # Output: integer მნიშვნელობა არის 12

#task 3
def sum_numbers(mixed_list):
    # ჩამოაყალიბებს ყველა ელემენტს სტრინგებსა და ინტეჯერებს შორის
    converted_numbers = [int(x) for x in mixed_list if isinstance(x, int) or (isinstance(x, str) and x.isdigit())]
    
    # აბრუნებს გადაქცეული რიცხვების ჯამს
    return sum(converted_numbers)

# მაგალითები
print(sum_numbers([10, "10"]))        # Output: 20
print(sum_numbers([5, "15", 20]))    # Output: 40
print(sum_numbers([1, "2", "three"]))  # Output: 3 (გამოიტოვებს არა ციფრულ სტრინგებს)
print(sum_numbers(["10", "20", "30"])) # Output: 60
