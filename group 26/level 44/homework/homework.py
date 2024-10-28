#Task 1
def min_and_max(arr):
    return [min(arr), max(arr)]

print(min_and_max([1, 2, 3, 4, 5]))  # აბრუნებს [1, 5]
print(min_and_max([-1, -2, -3, -4, -5]))  # აბრუნებს [-5, -1]
#Task 2
def is_empirical(n):
    # შევამოწმოთ, არის თუ არა n დადებითი მთელი რიცხვი
    if n <= 0:
        return False
    # გამოვიყენოთ pow ფუნქცია, რომ შევამოწმოთ, არის თუ არა n 2-ის ძლიერება
    power = 0
    while pow(2, power) < n:
        power += 1
    return pow(2, power) == n

print(is_empirical(2))   # დაბრუნებს True
print(is_empirical(4))   # დაბრუნებს True
print(is_empirical(6))   # დაბრუნებს False
print(is_empirical(8))   # დაბრუნებს True
print(is_empirical(16))  # დაბრუნებს True
