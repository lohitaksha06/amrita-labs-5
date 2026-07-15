def highest_occurring_char(text):
    
    
    text_lower = text.lower()
    
    char_count = {}
    
    for ch in text_lower:
        if 'a' <= ch <= 'z':
            if ch in char_count:
                char_count[ch] = char_count[ch] + 1
            else:
                char_count[ch] = 1
    
    if len(char_count) == 0:
        return None, 0
    
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count


if __name__ == "__main__":
    input_string = "hippopotamus"
    char, count = highest_occurring_char(input_string)
    print(f"Input string: \"{input_string}\"")
    print(f"Highest occurring character: '{char}'")
    print(f"Occurrence count: {count}")
