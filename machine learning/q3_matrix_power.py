# Question 3: Accept a square matrix A and positive integer m, return A^m
# Matrix multiplication logic done manually

def matrix_multiply(A, B):
    """Multiply two square matrices A and B of same size"""
    size = len(A)
    # Initialize result matrix with zeros
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    # Standard row-by-column multiplication
    for i in range(size):
        for j in range(size):
            total = 0
            for k in range(size):
                total = total + A[i][k] * B[k][j]
            result[i][j] = total
    
    return result


def matrix_power(A, m):
    """Raise square matrix A to power m (m is positive integer)"""
    size = len(A)
    
    # Start with identity matrix for multiplication
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    # Multiply A by itself m times
    for _ in range(m):
        result = matrix_multiply(result, A)
    
    return result


if __name__ == "__main__":
    # Example: 2x2 matrix
    A = [
        [1, 2],
        [3, 4]
    ]
    power = 3
    
    print("Matrix A:")
    for row in A:
        print(row)
    
    print(f"\nA raised to power {power}:")
    result_matrix = matrix_power(A, power)
    for row in result_matrix:
        print(row)
