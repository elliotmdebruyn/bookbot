def get_num_words(text):
    words = text.split()
    return len(words)

def count_occurance(text):
    counts = {}

    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1

    return counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    result = []
    for ch in num_chars_dict:
        item = {"char": ch, "num": num_chars_dict[ch]}
        result.append(item)
    result.sort(reverse=True, key=sort_on)
    return result