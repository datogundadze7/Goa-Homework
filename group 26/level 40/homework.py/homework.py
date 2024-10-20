def is_valid_ISBN10(isbn):
    # თუ ISBN-ის სიგრძე არაა 10 სიმბოლო, დაბრუნდება False
    if len(isbn) != 10:
        return False
    
    ჯამი = 0
    # გადამოწმება რომ პირველი 9 სიმბოლო იყოს რიცხვი და დათვლა ფორმულით
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        ჯამი += int(isbn[i]) * (10 - i)
    
    # თუ მე-10 სიმბოლო არის 'X', ის ითვლება როგორც 10
    if isbn[9] == 'X':
        ჯამი += 10
    # თუ ის რიცხვია, მაშინ მას პირდაპირ ვამატებთ
    elif isbn[9].isdigit():
        ჯამი += int(isbn[9])
    else:
        return False
    
    # ISBN უნდა იყოს გაყოფილი 11-ზე უვადოდ
    return ჯამი % 11 == 0

# მაგალითი ტესტებისთვის:
ტესტ_შემთხვევები = [
    "1112223339",  # ვალიდური ISBN-10
    "048665088X",  # ვალიდური ISBN-10
    "123456789X",  # ვალიდური ISBN-10
    "1234567890",  # არასწორი ISBN-10
    "abcdefghij",  # არასწორი ISBN-10
]

# ტესტების გაშვება
for isbn in ტესტ_შემთხვევები:
    print(f"{isbn}: {is_valid_ISBN10(isbn)}")
