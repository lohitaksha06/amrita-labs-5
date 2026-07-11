# Question 2: Find range (max-min) of a list of real numbers
# If list has less than 3 elements, return error message

def compute_range(numbers):
    """Takes a list and returns difference between max and min.
    If list has less than 3 items, returns an error string instead."""
    
    # Check if list has at least 3 elements
    if len(numbers) < 3:
        return "Range determination not possible"
    
    # Find min and max using built-in functions
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    
    return range_val


if __name__ == "__main__":
    sample_list = [5, 3, 8, 1, 0, 4]
    answer = compute_range(sample_list)
    print(f"List: {sample_list}")
    print(f"Range (max - min): {answer}")
    
    # Also test with short list to show error
    short_list = [2, 7]
    print(f"\nShort list: {short_list}")
    print(compute_range(short_list))
