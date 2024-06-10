#task 2
# შევქმენით სამი ცვლადი
num1 = 10
num2 = 5
num3 = 3

# მიმატება
addition_result = num1 + num2 + num3
print("Addition result:", addition_result)

# გამოკლება
subtraction_result = num1 - num2 - num3
print("Subtraction result:", subtraction_result)

# გამრავლება
multiplication_result = num1 * num2 * num3
print("Multiplication result:", multiplication_result)


# გაყოფა
split = num1 / num2 / num3
print("split:",split)



#task 3

# უნდა ვთხოვოთ მომხმარებელს შეიყვანოს მისი მონაცემები

first_name = input("Enter your first name: ")
last_name = input("Enter your last name:")
age = input("Enter your age:")
password = input("Enter your password:")

# შეყვანილი ინფორმაციის ჩვენება

print("User Account Details:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Password:", '*' * len(password))  

#პაროლის დაფარვა/დამალვა უსაფრთხოებისთვის

#task 4

# უნდა ვთხოვოთ მომხმარებელს შეიყვანონ თავიანთი მონაცემები

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
password = input("Enter your password: ")

# f-string-ის გამოყენებით 

print("\nUser Account Details:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"Password: {'*' * len(password)}")  

#პაროლის დაფარვა/დამალვა უსაფრთხოებისთვის

