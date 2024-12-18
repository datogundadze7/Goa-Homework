def valid_parentheses(string):
    # მშვენიერი ზოლების მექანიზმი
    count = 0
    for char in string:
        if char == '(':
            count += 1  # ახლის სახით აღებული მშვენიერი ზოლი
        elif char == ')':
            count -= 1  # დახურული მშვენიერი ზოლი
            if count < 0:  # თუ დახურული უფრო მეტია, ეს არასწორია
                return False
    return count == 0  # სწორია თუ ყველა ახლის შესატყვისი დახურულია

# ტესტები
test_cases = [
    "()",            # ვალიდური
    "(())",          # ვალიდური
    "(()())",        # ვალიდური
    "(()",           # არასწორი
    "())",           # არასწორი
    "())(",          # არასწორი
    "((())())",      # ვალიდური
    "())())",        # არასწორი
    "",              # ვალიდური (ცარიელი სტრიქონი ვალიდურია)
]

# შედეგების გადაცემა
results = [(s, valid_parentheses(s)) for s in test_cases]
print(results)
