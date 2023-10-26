import numpy as np
from matrix_operations import MatrixOperations  # Assuming your class is defined in matrix_operations.py

def main():
    # Example matrices
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    # Create MatrixOperations instances
    matrix_operations1 = MatrixOperations(matrix1)
    matrix_operations2 = MatrixOperations(matrix2)

    # Test addition function
    addition_result = matrix_operations1.addition(matrix_operations2)
    print("Addition Result:")
    print(addition_result)

    # Test subtraction function
    subtraction_result = matrix_operations1.subtraction(matrix_operations2)
    print("\nSubtraction Result:")
    print(subtraction_result)

    # Test multiplication function
    multiplication_result = matrix_operations1.multiplication(matrix_operations2)
    print("\nMultiplication Result:")
    print(multiplication_result)

    # Test transpose function
    print("\nOriginal Matrix:")
    matrix_operations1._printMatrix()  # Assuming you have the _printMatrix method implemented

    transposed_matrix = matrix_operations1.transpose()
    print("\nTransposed Matrix:")
    if transposed_matrix is not None:
        print(np.array_str(transposed_matrix))