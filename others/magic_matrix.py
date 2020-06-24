def is_magic(matrix):
    ismagic = 0
    indication = sum(matrix[0])
    if horizontal_check(matrix, indication):
        ismagic += 1
    if vertical_check(matrix, indication):
        ismagic += 1
    if not diagonal_check(matrix, indication):
        ismagic += 1
        
    if ismagic == 3:
        print('This matrix is magic')
    else:
        print('This matris isn\'t magic')
    
def horizontal_check(matrix, indication):
    ismagic = 0
    for row in matrix:
        if sum(row) == indication:
            ismagic += 1
    if ismagic == len(matrix):
        return True
    else:
        return False
    
    
def vertical_check(matrix, indication):
    ismagic = 0
    for num in range(0, len(matrix)):
        localnumber = 0
        for num2 in range(0, len(matrix)):
            localnumber += matrix[num2][num]
        if localnumber == indication:
            ismagic += 1
    if ismagic == len(matrix):
        return True
    else:
        return False        
    

def diagonal_check(matrix, indication):
    ismagic = 0
    localnumber = 0
    for num in range(len(matrix)):
        localnumber += matrix[num][num]
    if localnumber == indication:
        ismagic += 1
    localnumber = 0
    for i in range(len(matrix)):
        localnumber += matrix[i][len(matrix) - (i + 1)]
    if ismagic == 2:
        return True
    else:
        return False
    
    
    
    
    

matrix_true = [[2, 1, 3], [3, 2, 1], [1, 3, 2]]
matrix_false = [[2, 3, 2], [2, 3, 2], [2, 3, 2]]
is_magic(matrix_false)