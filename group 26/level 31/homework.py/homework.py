# 1) Spin Words - function to reverse words that have 5 or more letters
def spin_words(sentence):
    words = sentence.split()
    result = [word[::-1] if len(word) >= 5 else word for word in words]
    return ' '.join(result)

# 2) Count the smiley faces - function to count valid smiley faces in a list
def count_smileys(arr):
    valid_smileys = {':)', ';)', ':D', ';D', ':-)', ';-)', ':-D', ';-D', ':~)', ';~)', ':~D', ';~D'}
    return sum(1 for face in arr if face in valid_smileys)

# 3) Count characters that occur more than once - function to count duplicate characters in a string
from collections import Counter
def duplicate_count(text):
    counts = Counter(text.lower())
    return sum(1 for count in counts.values() if count > 1)

# Main function to demonstrate the tasks
def main():
    # Task 1: Spin Words
    sentence = "Hey fellow warriors"
    print(f"Original sentence: {sentence}")
    print(f"After spin_words: {spin_words(sentence)}")

    # Task 2: Count the smiley faces
    smiley_list = [':)', ';(', ';}', ':-D']
    print(f"Smiley list: {smiley_list}")
    print(f"Number of valid smiley faces: {count_smileys(smiley_list)}")

    # Task 3: Count duplicate characters
    text = "aabBcde"
    print(f"Text to check duplicates: {text}")
    print(f"Number of duplicate characters: {duplicate_count(text)}")

# Call the main function
if __name__ == "__main__":
    main()



def make_readable(seconds):
    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    # Return formatted string as HH:MM:SS
    return f"{hours:02}:{minutes:02}:{seconds:02}"
