    
# this file will have the solution of a problem where a list was given by BioUrja.
# that list was like [1,2,3,<>,1,2,3,<>,1,1,2] and we have to make a matrix out of it.
# and then check if the matrix is symmetric or not by checking if the matrix equate with it's 
# transpose. if it does then the given matrix is Symmetrix, otherwise it is not.

def buildMatrix(liss):
    breakCount = liss.count('<>')
    matrix = []
    temp = []
    count = 0
    for i in liss:
        if i == '<>':
            matrix.append(temp)
            temp = []
            continue
        temp.append(i)
    matrix.append(temp)
    return matrix

def transpose(matrix):
    row = len(matrix)
    column = len(matrix[0])
    result = [['0' for i in range(row)] for j in range(column)]
    for i in range(column):
        for j in range(row):
            result[i][j] = matrix[j][i]
    return result
inputList = ["1","2",'<>','2','1','<>','3','1','<>','4','4']


matrix = buildMatrix(inputList)
print(matrix)
print(transpose(matrix))
