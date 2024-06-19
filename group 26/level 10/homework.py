#Task 1

for number in range(1, 101):
    if number % 2 != 0:
        print(number)

#Task 2
number = 1
while number <= 1000:
    print(number)
    number += 1
#Task 3
number = 1
sum = 0

while number <= 10:
    sum += number
    number += 1

print("1-დან 10-მდე რიცხვების ჯამი არის:", sum)
#Task 4
#for ციკლის მაგალითები
#რიცხვების დაპრინტერება 1-დან 10-მდე, ყოველი რიცხვის კვადრატით:
for number in range(1, 11):
    print(f"{number} squared is {number ** 2}")
#ლუწი რიცხვების დაპრინტერება 2-დან 20-მდე:
for number in range(2, 21, 2):
    print(number)
#სტრიქონების ჩამოთვლა სიიდან:
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")
#სიტყვების თითო ასოს დაპრინტერება:
word = "python"
for letter in word:
    print(letter)
#რიცხვების დაპრინტერება უკუსვლით 10-დან 1-მდე:
for number in range(10, 0, -1):
    print(number)
#while ციკლის მაგალითები
#რიცხვების დაპრინტერება 1-დან 10-მდე ყოველი რიცხვის კუბით:
number = 1
while number <= 10:
    print(f"{number} cubed is {number ** 3}")
    number += 1
#რიცხვების დაპრინტერება 50-დან 60-მდე:
number = 50
while number <= 60:
    print(number)
    number += 1
#number = 50
while number <= 60:
    print(number)
    number += 1
#სიტყვების შერჩევა სიიდან შემთხვევითობით:
import random

words = ["hello", "world", "python", "code"]
index = 0
while index < len(words):
    print(words[index])
    index += random.randint(1, 2)
#რიცხვების დაპრინტერება 1-დან 20-მდე მხოლოდ ლუწი რიცხვებით:
number = 1
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1
#ფაქტორიალის გამოთვლა 1-დან 5-მდე:
number = 1
factorial = 1
while number <= 5:
    factorial *= number
    number += 1

print("Factorial of 5 is:", factorial)

