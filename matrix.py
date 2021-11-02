import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise(ValueError, "Vectors must be the same length.")

    sum_vectors = 0
    for i in range(len(vector_one)):
        sum_vectors += vector_one[i] * vector_two[i]
        
    return sum_vectors

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")

        return (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        return (self.g[0][0] + self.g[1][1])
                      
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        factor = 1 / self.determinant()
        trace_times_I = self.trace() * identity(2)
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

    def is_square(self):
        return self.h == self.w
    
    #-----OPERATOR OVERLOADING-----#
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for i_row in self.g:
            s += " ".join(["{} ".format(x) for x in i_row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrix_sum = []
        
        for i_row in range(self.h):
            row_result = []
            for i_col in range(other.w):
                row_result.append(self.g[i_row][i_col] + other.g[i_row][i_col])
 
            matrix_sum.append(row_result)
                
        return matrix_sum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg_matrix = []
        for i_row in range(self.h):
            row_result = []
            for i_col in range(self.w):
                row_result.append(self.g[i_row][i_col] * (-1))
                
            neg_matrix.append(row_result)
            
        return neg_matrix
                
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
            
        matrix_difference = []
        
        for i_row in range(self.h):
            row_result = []
            for col in range(other.w):
                row_result.append(self.g[i_row][i_col] - other.g[i_row][i_col])
                
            matrix_difference.append(row_result)
        
        return matrix_difference
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        
        if self.w != other.h:
            raise(ValueError, "The number of columns of Matrix A must equal the number of rows in Matrix B")
            
        matrix_product = []
        
#         [row[1] for row in A]
        
        for i_row in range(self.h):
            row_result = []
            for i_col in range(other.w):
                col_vals = [row[i_col] for row in other.g]
                row_result.append(dot_product(self.g[i_row], col_vals))
            matrix_product.append(row_result)
              

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            