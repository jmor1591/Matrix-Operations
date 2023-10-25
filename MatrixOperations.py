class MatrixOperations:
    def __init__(self,matrix):
        self._matrix = matrix

    def _get_num_rows(self):
        """
        Private functino to get the number of rows in the matrix
        """
        if not isinstance(matrix, list):
            print("Input is not a valid matrix.")
            return 0
        row_length = len(matrix)
        return row_length

    def _get_num_columns(self):
        """
        Private function to get the number of columns in the matrix.
        """
        if not isinstance(self._matrix, list) or not all(isinstance(row, list) for row in self._matrix):
            raise ValueError("Input is not a valid matrix (list of lists).")
        
        # Assuming all rows have the same number of columns
        if not self._matrix:
            return 0  # Return 0 for an empty matrix
        else:
            return len(self._matrix[0])
    
    def _same_size(self, other_matrix):
        """
        Private function to check if the current matrix and another matrix have the same size.
        """
        if self._get_num_rows() == other_matrix._get_num_rows() and self._get_num_columns() == other_matrix._get_num_columns():
            return True
        return False
    
    def addition(self.other)