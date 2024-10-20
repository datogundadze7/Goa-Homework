#manual_min()
def manual_min(numbers):
    # დავიწყებთ სიის პირველ ელემენტზე, როგორც მინიმალურ მნიშვნელობაზე
    min_value = numbers[0]
    # ვალუტებთ ყველა ელემენტს სიაში
    for num in numbers:
        # თუ ვპოულობთ უფრო მცირე რიცხვს, ვანახლებთ min_value-ს
        if num < min_value:
            min_value = num
    return min_value

# მაგალითი გამოყენებისათვის
my_list = [5, 2, 9, 1, 7]
print("მინიმალური რიცხვი არის:", manual_min(my_list))  # შედეგი: 1
#manual_max()
def manual_max(numbers):
    # დავიწყებთ სიის პირველ ელემენტზე, როგორც მაქსიმალურ მნიშვნელობაზე
    max_value = numbers[0]
    # ვალუტებთ ყველა ელემენტს სიაში
    for num in numbers:
        # თუ ვპოულობთ უფრო დიდ რიცხვს, ვანახლებთ max_value-ს
        if num > max_value:
            max_value = num
    return max_value

# მაგალითი გამოყენებისათვის
my_list = [5, 2, 9, 1, 7]
print("მაქსიმალური რიცხვი არის:", manual_max(my_list))  # შედეგი: 9
#manual_len()
def manual_len(lst):
    # საწყისი სიგრძე არის 0
    length = 0
    # გავდივართ სიის ყველა ელემენტზე
    for _ in lst:
        # ყოველი ელემენტის შემოწმებისას ვზრდით სიგრძეს ერთით
        length += 1
    return length

# მაგალითი გამოყენებისათვის
my_list = [5, 2, 9, 1, 7]
print("სიის სიგრძეა:", manual_len(my_list))  # შედეგი: 5
#manual_sum()
def manual_sum(lst):
    # საწყისი ჯამი არის 0
    total = 0
    # გავდივართ სიის ყველა ელემენტზე
    for num in lst:
        # ყოველი ელემენტის მნიშვნელობას ვუმატებთ საერთო ჯამს
        total += num
    return total

# მაგალითი გამოყენებისათვის
my_list = [5, 2, 9, 1, 7]
print("სიაში რიცხვების ჯამია:", manual_sum(my_list))  # შედეგი: 24
#task 3
text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)  # შედეგი: "hello Python"

def manual_replace(text, old, new):
    # აქ ვანაწევრებთ ტექსტს იმ ნაწილებზე, სადაც `old` ქვეცრია
    result = text.split(old)
    # შემდეგ ვაერთიანებთ იმ ნაწილებს `new` ქვეცრით
    return new.join(result)

# მაგალითი გამოყენებისათვის
text = "hello world, welcome to the world of programming"
new_text = manual_replace(text, "world", "Python")
print(new_text)  # შედეგი: "hello Python, welcome to the Python of programming"
#task 4
def manual_find(text, substring):
    # გავდივართ ტექსტის ყველა პოზიციაზე
    for i in range(len(text) - len(substring) + 1):
        # ვამოწმებთ, ემთხვევა თუ არა substring ტექსტის ამ პოზიციიდან
        if text[i:i + len(substring)] == substring:
            return i  # ვაბრუნებთ პირველ პოზიციას, სადაც ქვეცერი მოიძებნა
    return -1  # თუ ვერ მოიძებნა, ვაბრუნებთ -1-ს

# მაგალითი გამოყენებისათვის
text = "hello world"
position = manual_find(text, "world")
print(position)  # შედეგი: 6

position_not_found = manual_find(text, "Python")
print(position_not_found)  # შედეგი: -1
#task 5

# 1. L1: Set Alarm
def set_alarm(employed, vacation):
    return employed and not vacation

# 2. Thinkful - Logic Drills: Traffic light
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

# 3. Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 4. You're a square!
import math

def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

# 5. Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# 6. Array plus array
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

# 7. Grasshopper - Check for factor
def check_for_factor(base, factor):
    return base % factor == 0

# 8. Beginner - Lost Without a Map
def maps(a):
    return [x * 2 for x in a]