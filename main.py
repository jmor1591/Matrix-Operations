import numpy as np
from matrix_operations import MatrixOperations  # Assuming your class is defined in matrix_operations.py

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
print(matrix_operations1)

transposed_matrix = matrix_operations1.transpose()
print("\nTransposed Matrix:")
if transposed_matrix is not None:
    print(np.array_str(transposed_matrix))

# Test determinant function
    print("Determinant of Matrix 1:")
    determinant_result1 = matrix_operations1.determinant()
    print(determinant_result1)

    print("\nDeterminant of Matrix 2:")
    determinant_result2 = matrix_operations2.determinant()
    print(determinant_result2)

    # Test inverse function
    print("\nInverse of Matrix 1:")
    inverse_result1 = matrix_operations1.inverse()
    if inverse_result1 is not None:
        print(inverse_result1)

    print("\nInverse of Matrix 2:")
    inverse_result2 = matrix_operations2.inverse()
    if inverse_result2 is not None:
        print(inverse_result2)
    
    eigenvalues_result = matrix_operations1.eigenvalues()

    # Print the result
    if eigenvalues_result is not None:
        print("Eigenvalues of the Matrix:", eigenvalues_result)
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
    
print("Program finished")