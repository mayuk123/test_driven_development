class SparseMatrix:
    def __init__(self):
        # Initialize an empty dictionary to store non-zero elements of the sparse matrix
        self.data = {}

    def set(self, row, col, value):
        # Check for valid indices, rows and columns must be non-negative
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative.")
        
        # Set the value at (row, col) to 'value' if it's not zero
        if value != 0:
            self.data[(row, col)] = value

    def get(self, row, col):
        # Retrieve the value at (row, col) from the sparse matrix
        return self.data.get((row, col), 0)

    def recommend(self, vector):
        # Multiply the sparse matrix with 'vector' to produce recommendations
        recommendations = [0] * len(vector)
        for (row, col), value in self.data.items():
            # Multiply the value in the sparse matrix with the corresponding value in 'vector'
            recommendations[row] += value * vector[col]
        return recommendations

    def add_movie(self, matrix):
        # Add another sparse matrix, simulating the addition of a new movie
        for (row, col), value in matrix.data.items():
            # Set non-zero values from the new matrix into the current matrix
            self.set(row, col, value)

    def to_dense(self):
        # Convert the sparse matrix to a dense matrix
        max_row = max(row for row, _ in self.data.keys())
        max_col = max(col for _, col in self.data.keys())
        
        # Create a 2D list representing the dense matrix with appropriate dimensions
        dense_matrix = [[0] * (max_col + 1) for _ in range(max_row + 1)]
        
        # Populate the dense matrix with values from the sparse matrix
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        return dense_matrix






    
