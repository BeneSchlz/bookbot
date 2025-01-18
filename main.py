def main():
    # Path to the file
    path_to_file = "books/frankenstein.txt"
    
    # Open the file and read its contents
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    # Count words
    words = file_contents.split()
    word_count = len(words)
    
    # Count characters
    character_counts = count_characters(file_contents)
    
    # Generate and print the report
    generate_report(path_to_file, word_count, character_counts)

def count_characters(text):
    """
    Count the number of times each character appears in the text.
    Characters are converted to lowercase.
    Returns a dictionary where keys are characters and values are counts.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def generate_report(path_to_file, word_count, character_counts):
    """
    Print a formatted report of word and character counts.
    """
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert dictionary to a list of dictionaries for sorting
    sorted_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print character counts
    for char, count in sorted_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
