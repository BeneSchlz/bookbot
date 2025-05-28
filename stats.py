def num_words_text(text):
    words = text.split()
    num_words = 0
    for i in words:
        num_words += 1
    return num_words
 
def get_num_char(text):
    text = text.lower()  # Normalize to lowercase
    char_counts = {}     # Dictionary to hold character counts
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


