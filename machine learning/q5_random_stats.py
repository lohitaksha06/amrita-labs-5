# Question 5: Generate 25 random numbers between 1 and 10
# Find mean, median and mode of those numbers

import random

def generate_random_list(count, lower, upper):
    """Generate a list of random integers between lower and upper (inclusive)"""
    nums = []
    for _ in range(count):
        nums.append(random.randint(lower, upper))
    return nums


def compute_mean(numbers):
    """Average of all numbers in the list"""
    total = sum(numbers)
    return total / len(numbers)


def compute_median(numbers):
    """Middle value after sorting the list.
    If even number of elements, average of two middle values"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 1:
        # Odd number of elements - pick the middle one
        mid = n // 2
        return sorted_nums[mid]
    else:
        # Even number - average of two middle values
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (sorted_nums[mid1] + sorted_nums[mid2]) / 2


def compute_mode(numbers):
    """Find the value that appears most frequently.
    If multiple, returns the first one encountered with max frequency"""
    freq = {}
    
    # Count frequency of each number
    for num in numbers:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
    
    max_freq = max(freq.values())
    
    # Find which number has this max frequency
    for num in freq:
        if freq[num] == max_freq:
            return num


if __name__ == "__main__":
    random.seed()  # Use system time for randomness
    
    rand_list = generate_random_list(25, 1, 10)
    
    mean_val = compute_mean(rand_list)
    median_val = compute_median(rand_list)
    mode_val = compute_mode(rand_list)
    
    print(f"Generated 25 random numbers (1 to 10):")
    print(rand_list)
    print(f"\nMean:   {mean_val:.2f}")
    print(f"Median: {median_val}")
    print(f"Mode:   {mode_val}")
