import math
from math import sqrt
import numbers
########################################################################################################
def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)
########################################################################################################
def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
########################################################################################################
#get row for dot product

def get_row(matrix, row):
    return matrix[row]
########################################################################################################
#get column for dot product
def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])

    return column
########################################################################################################
#Dot product

def dot_product(vectorA, vectorB):
    result = 0
    
    for i in range(len(vectorA)):
        result += vectorA[i] * vectorB[i]
        
    return result
########################################################################################################
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
######################################################################################################## 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
           
        determinant = 0
        if self.h == 1:
            determinant = (self.g[0][0])
        elif self.h == 2:
            # Calculate the inverse of the square 1x1 or 2x2 matrix.
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            determinant = (a * d - b * c)
            
        return determinant                        
       
        
########################################################################################################
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        sum = 0
        
        for i in range(self.h):
            sum = sum + self.g[i][i]
           
        return sum
########################################################################################################
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
    
        inverse = []
        if self.h == 1:
            inverse.append([1 / self.g[0][0]])
        elif self.h == 2:
        # If the matrix is 2x2, check that the matrix is invertible
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
            # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1 / (a * d - b * c)
            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)            

########################################################################################################
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        transpose = []
        row = []
        
        for i in range(self.h):
            for j in range(self.w):
                row.append(self.g[j][i])
            transpose.append(row)
            row = []
            
        return Matrix(transpose)
########################################################################################################
    def is_square(self):
        return self.h == self.w
########################################################################################################
    #
    # Begin Operator Overloading
    ############################
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
########################################################################################################
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s
########################################################################################################
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrix_sum = []
        row = []
        
        for i in range(self.h):
            for j in range(self.w):
                row.append(self.g[i][j]+other.g[i][j])
            matrix_sum.append(row)
            row = []
            
        return Matrix(matrix_sum)
########################################################################################################        
        
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
        #   
        # TODO - your code here
        #
        
        # multiplying ever element with -1 meet the goal
########################################################################################################   
#         matrix_neg = []
#         row = []
        
#         for i in range(self.h):
#             for j in range(self.w):
#                 row.append((self.g[i][j])*-1)
#             matrix_neg.append(row)
#             row = []
            
#         return Matrix(matrix_neg)
########################################################################################################
#Method B

        negated_matrix = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self[i][j])
            negated_matrix.append(row)
            
        return Matrix(negated_matrix)
########################################################################################################

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
#adapted from the same code as for addition
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrix_sub = []
        row = []
        
        for i in range(self.h):
            for j in range(self.w):
                row.append(self.g[i][j]-other.g[i][j])
            matrix_sub.append(row)
            row = []
            
        return Matrix(matrix_sub)        
        
########################################################################################################
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
#######################################################################################################


        multi = zeroes(self.h, other.w)

        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    multi[i][j] += self.g[i][k] * other.g[k][j]

        return multi
#######################################################################################################
# # Multiplication of Matrix  𝐀  with matrix  𝐁  is only possible if the width of  𝐀  is equal to the height of  𝐁

#         if self.w != other.h:
#             raise(ValueError, "Matrices can only be subtracted if the width of First Matrix is equal to the height of Second Matrix") 
    
#         mult_sum = []
#         row = []
        
#         for i in range(self.h):
#             for in range(self.w):
#                 row.append((self.g[i][j])(other.g[i][j])+(self.g[i+1][j])(other.g[i][j+1]))

#######################################################################################################
#     def matrix_multiplication(matrixA, matrixB):
    
    # Store the number of rows in A and the number of columns in B.
    # This will be the size of the output matrix
#         m_rows = len(matrixA) ........replace m_rows with self.h
#         p_columns = len(matrixB[0]).......replace p_columns with self.w
    
#     # empty list that will hold the product of AxB
#         result = []
#     # For loop within a for loop. The outside for loop williterate through m_rows. The inside for loop will iterate  through p_columns.
#         for i in range(self.h):
#         # Accumulate the values of a row (reset each loop)
#             row_result = []
#         # Grab current A row
#             rowA = get_row(self.g, i)
#             for j in range(self.w):
                
#             # Grab current B column
#                 colB = get_column(other.g, j)
#             # Calculate the dot product of the A row and the B column
#                 dot_prod = dot_product(rowA, colB)
#             # And append to row_result
#                 row_result.append(dot_prod)
    
#         # Add the row_result to the result matrix
#             result.append(row_result) #tab

#         return Matrix(result)


########################################################################################################
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
        product = []
        
        if isinstance(other, numbers.Number):
#             pass
#             #   
#             # TODO - your code here
#             #
# assumption that other is a number that will be used for multiplication

            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self.g[i][j])
                product.append(row)
                
            return Matrix(product)
######################################################################################################
