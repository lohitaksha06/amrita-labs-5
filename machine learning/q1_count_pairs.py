# Question 1: Count pairs with sum equal to 10
# Given list: [2, 7, 4, 1, 3, 6]

def count_pairs_with_sum_ten(numbers):
    """Go through each pair in the list and count how many add up to 10"""
    pair_count = 0
    n = len(numbers)
    
    # Loop through all possible pairs using two indices
    for i in range(n):
        for j in range(i + 1, n):  # j starts from i+1 so we dont repeat pairs
            if numbers[i] + numbers[j] == 10:
                pair_count = pair_count + 1
    
    return pair_count


if __name__ == "__main__":
    nums = [2, 7, 4, 1, 3, 6]
    result = count_pairs_with_sum_ten(nums)
    print(f"Given list: {nums}")
    print(f"Number of pairs with sum 10: {result}")
