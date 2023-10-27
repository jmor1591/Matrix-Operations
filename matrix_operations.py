import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Invalid matrix format.")
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
    
    def _proper(self):
        if not isinstance(self.matrix, list) or not all(isinstance(row, list) for row in self.matrix):
            print("Invalid matrix format.")
            return False
        return True

    """
    Unneeded function, print(matrix) works fine
    def _printMatrix(self):
        # Private function to print a matrix
        if isinstance(self.matrix, list) and self.matrix:
            print(np.array_str(self.matrix))
        else:
            print("Invalid or empty matrix format.")
    """

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
    
    def determinant(self):
        """
        Function to calculate the determinant of a matrix
        """
        if not isinstance(self.matrix, list) or not all(isinstance(row,list) for row in self.matrix):
            print("Invalid matrix format.")
            return None
        
        try:
            det = np.linalg.det(self.matrix)
            return det
        except np.linalg.LinAlgError:
            print("Matrix is not singular, determinant cannot be found")
            return None
    
    def inverse(self):
        """
        Function to compute the inverse of a matrix
        """
        determinant = self.determinant()
        if determinant == 0:
            print("Matrix is singular and cannot be inverted")
            return None
        
        try:
            inverse_matrix = np.linalg.inv(self.matrix)
            return inverse_matrix
        except np.linalg.LinAlgError:
            print("Error occurred while computing the inverse")
    
    def eigenvalues(self):
        """
        Function to compute the eigenvalues of the matrix.
        """
        if not isinstance(self.matrix, list) or not all(isinstance(row, list) for row in self.matrix):
            print("Invalid matrix format.")
            return None
        
        try:
            eigenvalues = np.linalg.eigvals(self.matrix)
            return eigenvalues
        except np.linalg.LinAlgError:
            print("Error occurred while computing the eigenvalues.")
            return None
    
    def eigenvectors(self, eigenvalues):
        """
        Compute the eigenvectors corresponding to given eigenvalues.

        Args:
            eigenvalues (list): List of eigenvalues for which eigenvectors are computed.

        Returns:
            list: A list of numpy arrays representing the eigenvectors corresponding to the given eigenvalues.
                  Each array represents an eigenvector.
                  Returns None if there's an error during computation.
        """
        if not isinstance(self.matrix, list) or not all(isinstance(row, list) for row in self.matrix):
            print("Invalid matrix format.")
            return None
        
        try:
            eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
            selected_eigenvectors = []
            for eigenvalue in eigenvalues:
                if eigenvalue in eigenvalues:
                    index = np.where(eigenvalues == eigenvalue)[0][0]
                    selected_eigenvectors.append(eigenvectors[:, index])
            return selected_eigenvectors
        except np.linalg.LinAlgError:
            print("Error occurred while computing the eigenvectors.")
            return None
