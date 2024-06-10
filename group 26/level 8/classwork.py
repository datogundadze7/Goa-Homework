#Task 1
# მომხმარებელს მიეცემა რიცხვები
num1 = float(input("Enter the value of num1:"))
num2 = float(input("Enter the value of num2:"))

# num1-ის შემოწმება, რომ მეტია num2-ზე
if num1 > num2:
    print("num1 is greater than num2")
# num1-ის შემოწმება, რომ ნაკლებია num2-ზე
elif num1 < num2:
    print("num1 less than num2-ზე")
# num1-ის შემოწმება, რომ ტოლია num2-ს
else:
    print("num1 eqqual num2-ს")

#Task 2
# მომხმარებელს მიეცემა რიცხვები
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

# num1-ის და num2-ს შემოწმება, რომ ორივე დასრულებულია
if num1 > 0 and num2 > 0:
    print("Their results are confirmed")
else:
    print("Their results are not confirmed")

# num1-ის ან num2-ის შემოწმება, რომ ერთი ან ორი დასრულებულია
if num1 > 0 or num2 > 0:
    print("There is one or two proofs")
else:
    print("There is nothing wrong with it")

#Task 3
# ღირებულებების შემოწმება
num1 = 5
num2 = 10

#  num1 ნაკლებია num2
result1 = num1 < num2

# num1 მეტია num2
result2 = num1 > num2

#  num1 ტოლია  num2
result3 = num1 == num2

# გამოგვაქვს შედეგი
print("num1 < num2:", result1)
print("num1 > num2:", result2)
print("num1 == num2:", result3)

