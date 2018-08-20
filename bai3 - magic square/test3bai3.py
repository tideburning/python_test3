def isMagicSquare( mat) :
    # check square matrix
    rows = len(mat)
    for row in mat:
        if len(mat) != rows:
            return False 
    # calculate the sum of the prime diagonal
    s = 0
    for i in range(0, len(mat)) :
        s = s + mat[i][i]
    
    # For sums of Rows 
    for i in range(0, len(mat)) :
        rowSum = 0;     
        for j in range(0, (len(mat))) :
            rowSum += mat[i][j]
         
        # check if every row sum is equal to prime diagonal sum
        if (rowSum != s) :
            return False
 
    # For sums of Columns
    for i in range(0, len(mat)):
        colSum = 0
        for j in range(0, len(mat)) :
            colSum += mat[j][i]
 
        # check if every column sum is equal to prime diagonal sum
        if (s != colSum) :
            return False
 
    return True
 
# Driver Code
import numpy as np
matrix = np.array([ [2, 7, 6],
                    [9, 5, 1],
                    [4, 3, 8] ])
     
if (isMagicSquare(matrix)) :
    print( "Magic Square")
else :
    print( "Not a magic Square")

