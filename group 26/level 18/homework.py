def sum_two_numbers(a, b):
    """
    ფუნქცია, რომელიც გამოიტანს ორი რიცხვის ჯამს.
    """
    return a + b

# მაგალითი გამოყენებისთვის
number1 = 5
number2 = 10

# გამოიტანეთ ჯამი
result = sum_two_numbers(number1, number2)
print(f"ჯამი {number1} და {number2} არის: {result}")
#task 2 
def multiply_three_numbers(a, b, c):
    """
    ფუნქცია, რომელიც გამოიტანს სამი რიცხვის ნამრავლს.
    """
    return a * b * c

# მაგალითი გამოყენებისთვის
number1 = 2
number2 = 3
number3 = 4

# გამოიტანეთ ნამრავლი
result = multiply_three_numbers(number1, number2, number3)
print(f"{number1}, {number2} და {number3} ნამრავლი არის: {result}")
#task 3
def greet(first_name, last_name):
    """
    ფუნქცია, რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას.
    """
    greeting = f"გამარჯობა, {first_name} {last_name}!"
    return greeting

# მაგალითი გამოყენებისთვის
first_name = "დათო"
last_name = "გუნდაძე"

# გამოიტანეთ მისალმება
print(greet(first_name, last_name))
#task 4
def sum_two_numbers(a, b):
    """
    ფუნქცია, რომელიც დააბრუნებს ორი რიცხვის ჯამს.
    """
    return a + b

# მაგალითი გამოყენებისთვის
number1 = 7
number2 = 3

# მიღებული მნიშვნელობა მიანიჭეთ ცვლადს
result = sum_two_numbers(number1, number2)

# გამოიტანეთ შედეგი
print(f"ჯამი {number1} და {number2} არის: {result}")
#task 5
def multiply_three_numbers(a, b, c):
    """
    ფუნქცია, რომელიც დააბრუნებს სამი რიცხვის ნამრავლს.
    """
    return a * b * c

# მაგალითი გამოყენებისთვის
number1 = 4
number2 = 5
number3 = 6

# მიღებული მნიშვნელობა მიანიჭეთ ცვლადს
result = multiply_three_numbers(number1, number2, number3)

# გამოიტანეთ შედეგი
print(f"{number1}, {number2} და {number3} ნამრავლი არის: {result}")
#task 6
def print_food_list(food_list):
    """
    ფუნქცია, რომელიც არგუმენტად მიღებულ საჭმელების list-ს გამოიტანს თითოეულ საჭმელს ცალ-ცალკე.
    """
    for food in food_list:
        print(food)

# მაგალითი გამოყენებისთვის
foods = ["პიცა", "ბურგერი", "პასტა", "სალათი", "შოკოლადი"]

# გამოიტანეთ საჭმელები
print_food_list(foods)
#task 7
def print_number_list(number_list):
    """
ფუნქცია, რომელიც არგუმენტად მიღებულ რიცხვების list-ს გამოიტანს თითოეულ რიცხვს ცალ-ცალკე.
    """
    for number in number_list:
        print(number)

# მაგალითი გამოყენებისთვის
numbers = [10, 20, 30, 40, 50]

# გამოიტანეთ რიცხვები
print_number_list(numbers)

