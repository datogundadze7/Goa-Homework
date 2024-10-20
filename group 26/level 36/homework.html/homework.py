# Example list containing lists of numbers
list_of_lists = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Function to calculate the average of each list
def calculate_averages(lists):
    averages = []
    for inner_list in lists:
        if inner_list:  # Check if the inner list is not empty
            avg = sum(inner_list) / len(inner_list)
            averages.append(avg)
    return averages

# Calculate averages and print the result
result = calculate_averages(list_of_lists)
print("Averages of each inner list:", result)
