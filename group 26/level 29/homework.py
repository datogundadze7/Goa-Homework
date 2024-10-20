# Dictionary-ს შექმნა
my_dict = {
    "name": "Datex",
    "age": 25,
    "city": "Benze"
}

# For loop-ით key და value წყვილების გამოტანა
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
#task 2
# სამი მანქანის ინფორმაცია dictionary-ს სახით
cars = {
    "Car1": {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price": "$25,000"
    },
    "Car2": {
        "make": "Honda",
        "model": "Civic",
        "year": 2022,
        "price": "$22,000"
    },
    "Car3": {
        "make": "Ford",
        "model": "Mustang",
        "year": 2021,
        "price": "$30,000"
    }
}

# მანქანის შესახებ ინფორმაციის წარმოჩენა
for car, details in cars.items():
    print(f"გთავაზობთ მანქანას: {car}")
    print(f"მწარმოებელი: {details['make']}")
    print(f"მოდელი: {details['model']}")
    print(f"წელი: {details['year']}")
    print(f"ფასი: {details['price']}")
    print()  # ცარიელი ხაზის დამატება თითოეული მანქანის შემდეგ

#task 3
