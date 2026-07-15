def matrix_multiply(A, B):
    
    size = len(A)
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            total = 0
            for k in range(size):
                total = total + A[i][k] * B[k][j]
            result[i][j] = total
    
    return result


def matrix_power(A, m):
   
    size = len(A)
    
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    for _ in range(m):
        result = matrix_multiply(result, A)
    
    return result


if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
]
    power = 3
    
    print("Matrix A:")
    for row in A:
        print(row)
    
    print(f"\nay raised to power {power}:")
    result_matrix = matrix_power(A, power)
    for row in result_matrix:
        print(row)
