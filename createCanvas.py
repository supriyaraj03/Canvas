# -*- coding: utf-8 -*-
import sys
import wrapper

#############################################
# Create a canvas of desired width and height
#############################################
def create_Canvas(inputVal):
    split_input = str.split(inputVal , ' ')
    
    try:
        width = int(split_input[1])
        height = int(split_input[2])
        if((width <= 0) or (height <= 0)):
            sys.exit('Width and height should be positive integer')
    except ValueError:
        sys.exit('Width and height should be positive integer')
    
    matrix = [[' ' for x in range(width)] for y in range(height+2)] 
    for i in range(0,height+2):
        if((i == 0) or (i == height+1)):
            for j in range(0,width):
                matrix[i][j] = '-'
        else:
            matrix[i][0] = '|'
            matrix[i][width-1] = '|'
    wrapper.printFunction(matrix , height)
    print(matrix)
    return(matrix)
