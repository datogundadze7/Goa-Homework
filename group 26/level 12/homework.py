#task 1
import random

# შემთხვევითი რიცხვის გენერაცია 1-დან 10-ის ჩათვლით
correct_number = random.randint(1, 10)

while True:
    user_input = int(input("შეიყვანეთ რიცხვი 1-დან 10-ის ჩათვლით: "))
    
    if user_input == correct_number:
        print("სწორია!")
        break
    else:
        print("არასწორია, სცადეთ ისევ.")
#task 2
# ნამრავლის საწყისი მნიშვნელობა
product = 1

# საწყისი რიცხვი
number = 1

# while ციკლი 1-დან 10-ის ჩათვლით რიცხვების ნამრავლის გამოსათვლელად
while number <= 10:
    product *= number
    number += 1

print("1-დან 10-ის ჩათვლით რიცხვების ნამრავლი არის:", product)
#task 3
while True:
    # მომხმარებელს რიცხვის შეყვანა
    user_input = input("შეიყვანეთ რიცხვი (ან დაწერეთ 'exit' გასასვლელად): ")

    # პროგრამიდან გამოსვლა
    if user_input.lower() == 'exit':
        print("პროგრამა დასრულდა.")
        break

    # რიცხვის ტექსტიდან რიცხვში გადაყვანა
    try:
        number = int(user_input)
    except ValueError:
        print("გთხოვთ შეიყვანეთ ვალიდური რიცხვი.")
        continue

    # რიცხვის ლუწი ან კენტი შემოწმება
    if number % 2 == 0:
        print("რიცხვი ლუწია.")
    else:
        print("რიცხვი კენტია.")
#task 4
# მომხმარებლისგან ქულის შეყვანა
score = int(input("შეიყვანეთ ქულა (0-დან 100-ის ჩათვლით): "))

# ქულის მიხედვით შეფასების განსაზღვრა
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 50 <= score <= 59:
    grade = "E"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "არასწორი ქულა. გთხოვთ შეიყვანოთ 0-დან 100-ის ჩათვლით რიცხვი."

print(f"თქვენი ქულაა {score}, შეფასება: {grade}")
