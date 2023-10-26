import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def _get_num_rows(self):
        """
        Private function to get the number of rows in the matrix
        """
        if not isinstance(self.matrix, list):
            print("Input is not a valid matrix.")
            return 0
        return len(self.matrix)

    def _get_num_columns(self):
        """
        Private function to get the number of columns in the matrix.
        """
        if not isinstance(self.matrix, list) or not all(isinstance(row, list) for row in self.matrix):
            raise ValueError("Input is not a valid matrix (list of lists).")
        return len(self.matrix[0])

    def _same_size(self, other_matrix):
        """
        Private function to check if the current matrix and another matrix have the same size.
        """
        if self._get_num_rows() == other_matrix._get_num_rows() and self._get_num_columns() == other_matrix._get_num_columns():
            return True
        return False

    def _printMatrix(self):
        """
        Private function to print a matrix
        """
        if isinstance(self.matrix, list):
            print(np.array_str(self.matrix))
        else:
            print("Invalid or empty matrix format.")


    def addition(self,other):
        """Function that adds two matrices together"""
        if not self._same_size(other):
            return "Matrices not the same size"
        result = np.add(self.matrix, other.matrix)
        return result

    def subtraction(self, other):
        """Function that subtracts the first matrix from the second matrix"""
        if not self._same_size(other):
            return "Matrices not the same size"
        result = np.subtract(self.matrix, other.matrix)
        return result

    def multiplication(self, other):
        """Function for matrix multiplication"""
        if self._get_num_columns() != other._get_num_rows():
            return "Invalid dimensions for matrix multiplication"
        result = np.dot(self.matrix, other.matrix)
        return result
    
    def transpose(self):
        """
        Function to calculate the transpose of the matrix.
        """
        if isinstance(self.matrix, list):
            # If the matrix is a list of lists, perform the transpose operation
            transposed_matrix = np.transpose(self.matrix)
            return transposed_matrix
        else:
            # If the matrix is not in the correct format, print an error message
            print("Invalid matrix format. Transpose operation cannot be performed.")
            return None