def count_pairs_with_sum_ten(numbers):
    
    pair_count = 0
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == 10:
                pair_count = pair_count + 1
    
    return pair_count


if __name__ == "__main__":
    nums = [2, 7, 4, 1, 3, 6]
    result = count_pairs_with_sum_ten(nums)
    print(f"Given list: {nums}")
    print(f"Number of pairs with sum 10: {result}")
