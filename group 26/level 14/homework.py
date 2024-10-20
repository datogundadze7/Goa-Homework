# Original list
list1 = [2, 51, 11, 13, 51, 100]

# 1. Output every item from list with positive indexing
print("Positive indexing:")
for i in range(len(list1)):
    print(list1[i])

# 2. Output every item from list with negative indexing
print("\nNegative indexing:")
for i in range(-1, -len(list1)-1, -1):
    print(list1[i])

# 3. Replace the last element of a list with a new value
list1[-1] = 200
print("\nList after replacing the last element:", list1)

# 4. Replace the fifth element of a list with a new value
list1[4] = 99
print("List after replacing the fifth element:", list1)

# 5. Extract the last three elements of a list
last_three_elements = list1[-3:]
print("Last three elements:", last_three_elements)

# 6. Extract the first three elements of a list
first_three_elements = list1[:3]
print("First three elements:", first_three_elements)

# 7. Extract the middle two elements of a list
middle_two_elements = list1[2:4]
print("Middle two elements:", middle_two_elements)

# 8. Extract random elements of a list with negative indexes
# Example: Extracting elements at positions -2 and -4
random_negative_indexes = [list1[-2], list1[-4]]
print("Random elements with negative indexes:", random_negative_indexes)
