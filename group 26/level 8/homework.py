#Task 1
if a !=b:
 print("a is equal to b")
if a >= b:
 print("a is greater than or equal to b")
if a <=b:
 print("a is not or equal to b")

#Task 2
# ცვლადების გამოყენებით შედარება
a = 5
b = 3
c = 5

# შედარება ერთმანეთით
if a == b:
        print("a is equal to b")
else:
      print("a is not equal to b")

# შედარება სხვადასხვა მნიშვნელობებზე
if a != b:
   print("a is not equal to b")
else:
      print("a is equal to b")

# შედარება მეტი ან ტოლი
if a >= c:
    print("a is greater than or equal to c")
else:
     print("a is less than c")
# შედარება ნაკლები ან ტოლი
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is greater than b")

# შედარება მეტი
if a > b:
    print("a is greater than b")
else:
    print("a is less than or equal to b")

# შედარება ნაკლები
if a < c:
    print("a is less than c")
else:
   print("a is greater than or equal to c")

# ლოგიკური "and" ოპერატორი
if a > b and a > c:
   print("a is greater than b and c")
else:
   print("a is not greater than b and c")
# ლოგიკური "or" ოპერატორი
if a > b or a > c:
   print("a is greater than b or c")
else:
   print("a is not greater than b and c")

#Task 3
#ოპერატორი "or" ის წესია საშუალებას უზრუნველყოფს, რომ ერთი ან ორი მნიშვნელობა ჭეშმარიტია, ანუ ერთ-ერთი შედეგით მისი პირველადი ტერმინალია ჭეშმარიტი.
# x არც მეტია ან ტოლია 0-ს და y-ს
if x <= 0 or x <= y:
    print("x is not greater than or equal to 0 and y")

#ოპერატორი "and" წესია საშუალებას უზრუნველყოფს, რომ ორი მნიშვნელობა ჭეშმარიტია მხოლოდ მაშინ, როცა ერთიც და მეორეც ჭეშმარიტია. მაგალითად:
x = 5
y = 10
z = 15

# x მეტია იდენტურია და y-ზე და x მეტია იდენტურია და z-ზე
if x > 0 and x > y:
   print("x is greater than 0 and x is greater than y")

# ერთი მხოლოდ ან ოპერატორის ჩატარებით საკმაოდ ცდილობს და ყოველი შედეგისთვის ახალი დაშვებას შექმნის
if x > 0 or x > y:
   print("strange only one sequence is quite calculated")

#Task 4

# მომხმარებელს მიეცემა საკუთარი რიცხვები
num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))
# num1-ის შემოწმება, რომ მეტია num2-ზე
if num1 > num2:
    print("num1 is greater than num2")
# num1-ის შემოწმება, რომ ნაკლებია num2-ზე
elif num1 < num2:
    print("num1 is less than num2")
# num1-ის შემოწმება, რომ ტოლია num2-ს
else:
    print("num1 is equal to num2")