#task 1
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# მაგალითი გამოყენების:
numbers = [4, 8, 15, 16, 23, 42]
print(average(numbers))  # 18.0
#task 2
def manual_abs(x):
    if x < 0:
        return -x
    return x

# მაგალითი გამოყენების:
print(manual_abs(-5))  # 5
print(manual_abs(3))   # 3
print(manual_abs(0))   # 0
#task 3
# 1) ფუნქცია რომელიც გამოიტანს რიცხვების საშუალო არითმეტიკულს
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# 2) ფუნქცია რომელიც აბრუნებს რიცხვის აბსოლუტურ მნიშვნელობას
def manual_abs(x):
    if x < 0:
        return -x
    return x

# 3) ფუნქცია რომელიც გამოიტანს ლისტს დუპლიკატების გარეშე
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# ტესტირება
numbers = [4, 8, 15, 16, 23, 42]
print("Average:", average(numbers))  # 18.0

print("Manual abs of -5:", manual_abs(-5))  # 5
print("Manual abs of 3:", manual_abs(3))   # 3

input_list = [1, 2, 3, 1]
output_list = remove_duplicates(input_list)
print("List without duplicates:", output_list)  # [1, 2, 3]
#task 4
# 1) Descending Order
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

# 2) Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# 3) Get the Middle Character
def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid-1:mid+1]

# 4) Shortest Word
def find_short(s):
    return min(len(word) for word in s.split())

# 5) Square Every Digit
def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

# 6) Isograms
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# ტესტირება
print(descending_order(42145))  # 54421
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))  # 13
print(get_middle("testing"))  # "t"
print(find_short("bitcoin take over the world maybe who knows perhaps"))  # 3
print(square_digits(9119))  # 811181
print(is_isogram("Dermatoglyphics"))  # True
print(is_isogram("aba"))  # False
