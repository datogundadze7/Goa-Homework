#task 1
# მომხმარებლისგან ასაკის შეყვანა
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# ასაკის მიხედვით შეტყობინების განსაზღვრა
if age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
else:
    print("You are grown up")
#task 2
# საწყისი რიცხვი
number = 1

# while ციკლი 1-დან 100-მდე რიცხვების გამოსატანად
while number <= 100:
    if 40 <= number <= 50:
        number += 1
        continue
    print(number)
    number += 1
