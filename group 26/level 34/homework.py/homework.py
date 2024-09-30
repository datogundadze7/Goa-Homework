# 2. მაგალითი: try-except
try:
    temperature = float(input("Enter the temperature in Celsius: "))
    print("Temperature in Fahrenheit:", (temperature * 9/5) + 32)
except ValueError:
    print("Please enter a valid numerical value for temperature.")


# 3. მაგალითი: try-except-finally
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    print("You are eligible to enter.")
except ValueError as e:
    print("Error:", e)
finally:
    print("Program ended.")


# 4. მაგალითი: try-except-else
try:
    filename = input("Enter the filename: ")
    file = open(filename, "r")
except FileNotFoundError:
    print("File not found! Please check the file name.")
else:
    print("File opened successfully.")
    print(file.read())
    file.close()
