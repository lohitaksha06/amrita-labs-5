# Question 4: Count highest occurring character and its count in a string
# Only alphabets are considered, ignore numbers/symbols/spaces

def highest_occurring_char(text):
    """Find which alphabet character appears most often and how many times.
    Only letters a-z and A-Z are considered."""
    
    # Convert to lowercase so 'A' and 'a' are treated as same
    text_lower = text.lower()
    
    # Dictionary to store count of each alphabet character
    char_count = {}
    
    # Loop through each character in the string
    for ch in text_lower:
        # Check if character is an alphabet (a to z)
        if 'a' <= ch <= 'z':
            if ch in char_count:
                char_count[ch] = char_count[ch] + 1
            else:
                char_count[ch] = 1
    
    # If no alphabets found, return None for both
    if len(char_count) == 0:
        return None, 0
    
    # Find the character with maximum count
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count


if __name__ == "__main__":
    input_string = "hippopotamus"
    char, count = highest_occurring_char(input_string)
    print(f"Input string: \"{input_string}\"")
    print(f"Highest occurring character: '{char}'")
    print(f"Occurrence count: {count}")
