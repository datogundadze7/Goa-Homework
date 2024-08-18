#task 1
# შევქმენით integerების list'ი
numbers = [1, 2, 3, 4, 5]

# გადავატარეთ for loop'ი
for number in numbers:
    # თითოეული რიცხვი გამრავლებული ორზე
    result = number * 2
    # გამოიტანეთ შედეგი
    print(result)
#task 2
# შევქმენით string'ების list'ი
list1 = ["data", "luka"]

# გადავატარეთ for loop'ი
for word in list1:
    # თითოეული სიტყვა თავში "#"ით
    result = "#" + word
    # გამოიტანეთ შედეგი
    print(result)
#task 3
# შექმენით 2 list'ი 3-3 ელემენტებით
list1 = ["nika", "luka", "gio"]
list2 = ["data", "beqa", "gigi"]

# შეაერთეთ 2 list
combined_list = list1 + list2

# გამოიტანეთ შედეგი
print(combined_list)
#task 4
# შექმენით string'ი 10 სიტყვით
sentence = "The quick brown fox jumps over the lazy dog quickly."

# შექმენით ცალკეული სიტყვების ცვლადები slicing-ის მეშვეობით
word1 = sentence.split()[0]
word2 = sentence.split()[1]
word3 = sentence.split()[2]
word4 = sentence.split()[3]
word5 = sentence.split()[4]
word6 = sentence.split()[5]
word7 = sentence.split()[6]
word8 = sentence.split()[7]
word9 = sentence.split()[8]
word10 = sentence.split()[9]

# გამოიტანეთ თითოეული ცვლადი
print("Word 1:", word1)
print("Word 2:", word2)
print("Word 3:", word3)
print("Word 4:", word4)
print("Word 5:", word5)
print("Word 6:", word6)
print("Word 7:", word7)
print("Word 8:", word8)
print("Word 9:", word9)
print("Word 10:", word10)
