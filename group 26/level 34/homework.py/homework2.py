def sum_mixed_numbers(numbers):
    # ვცდილობთ თითოეული ელემენტი გარდავქმნათ რიცხვად (თუ შესაძლებელია)
    clean_numbers = [int(num) for num in numbers if isinstance(num, (int, str)) and str(num).isdigit()]
    return sum(clean_numbers)

# მაგალითი გამოყენებისათვის
numbers = [10, "10", "abc", 20, "30", "xyz"]
print(sum_mixed_numbers(numbers))  # შედეგი: 70
