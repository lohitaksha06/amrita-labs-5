def compute_range(numbers):
    
    
    if len(numbers) < 3:
        return "range determination not possible"
    
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    
    return range_val


if __name__ == "__main__":
    sample_list = [5, 3, 8, 1, 0, 4]
    answer = compute_range(sample_list)
    print(f"List: {sample_list}")
    print(f"Range (max - min): {answer}")
    
    short_list = [2, 7]
    print(f"\nsshort list: {short_list}")
    print(compute_range(short_list))
