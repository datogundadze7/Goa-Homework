import math

# 1. ყველა რიცხვის 5-ით გამრავლება
numbers = [1, 2, 3, 4, 5]
multiplied_by_5 = list(map(lambda x: x * 5, numbers))
print("1. 5-ით გამრავლებული რიცხვები:", multiplied_by_5)

# 2. სტრინგების ჩამონათვალის ჩაწერა inteiro სახით
string_numbers = ["1", "2", "3"]
converted_to_integers = list(map(int, string_numbers))
print("2. რიცხვები inteiro სახით:", converted_to_integers)

# 3. სიტყვების ჩამონათვალზე "!"-ის დამატება
words = ["hello", "world"]
words_with_exclamation = list(map(lambda word: word + "!", words))
print("3. სიტყვები '!' ზარის დამატებით:", words_with_exclamation)

# 4. რიცხვების კვადრატული ფესვების გამოთვლა
numbers_to_sqrt = [1, 4, 9, 16, 25]
square_roots = list(map(math.sqrt, numbers_to_sqrt))
print("4. კვადრატული ფესვები:", square_roots)

# 5. სია booleans, რომელიც მიუთითებს რიცხვების წყვილი ან უარი გამოხატულებაზე
numbers_to_check = [1, 2, 3, 4, 5]
even_or_odd = list(map(lambda x: x % 2 == 0, numbers_to_check))
print("5. წყვილი ან უარი:", even_or_odd)
