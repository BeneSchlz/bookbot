def character_count(text):
    text = text.lower()  # Convert text to lowercase
    count_dict = {}      # Dictionary to store character counts

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            count_dict[char] = count_dict.get(char, 0) + 1

    return count_dict

# Read the content of frankenstein.txt
with open("books/frankenstein.txt", "r") as file:
    content = file.read()
    print(content)

# Count the words
words = len(content.split())
print("Word count:", words)

# Count the characters
characters = len(content)
print("Character count:", characters)

# Count each character's occurrences
char_counts = character_count(content)
print("Character frequency:", char_counts)

print("=== Book Report: Frankenstein ===")
print(f"Total Word Count: {words}")
print(f"Total Character Count (including spaces): {characters}")
print("\nCharacter Frequency (only alphabetic characters):")
for char, count in sorted(char_counts.items()):
    print(f"{char}: {count}")
