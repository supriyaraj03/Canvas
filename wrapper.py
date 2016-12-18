# -*- coding: utf-8 -*-
import sys
import drawLine
import drawRectangle
import createCanvas


#############################################
# Used to print the matrix in a canvas format
#############################################
def printFunction(matrix , height):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()
        

####################################
# User input validation is performed
####################################
def validateInput(input_var , firstCommand=False):
    if (input_var == 'Q'):
            sys.exit('Program Exiting')                

    split_input = str.split(input_var , ' ')
    if(firstCommand):
        if (split_input[0] != 'C' or len(split_input) != 3):
            sys.exit('Format error. Input should be of type \'C w h\'')
    else:
        if (split_input[0] != 'C' and 
            split_input[0] != 'B' and 
            split_input[0] != 'L' and
            split_input[0] != 'R' ):
            sys.exit('User input error')
            if (split_input[0] == 'C' and len(split_input)!=3):
                sys.exit('Format error. Input should be of type \'C w h\' to create a canvas')                
            if (split_input[0] == 'L' and len(split_input)!=5):
                sys.exit('Format error. Input should be of type \'L x1 y1 x2 y2\' to draw a line')
            if (split_input[0] == 'R' and len(split_input)!=5):
                sys.exit('Format error. Input should be of type \'R x1 y1 x2 y2\' to draw a rectangle')
            if (split_input[0] == 'B' and len(split_input)!=5):
                sys.exit('Format error. Input should be of type \'B x y c\' for bucket fill')
                
##########################################################################
# Perform the required operation
# Current supported operations: draw canvas straight line, rectangle, quit
##########################################################################
def performOperation(inputVal , canvas=False):
    if (inputVal[0] == 'C'):
        op = createCanvas.create_Canvas(inputVal)
    elif (inputVal[0] == 'L'):
        op = drawLine.createLine(inputVal , canvas)
    elif (inputVal[0] == 'R'):
        op = drawRectangle.createRectangle(inputVal , canvas)
    elif (inputVal[0] == 'B'):
        print("Needs clarification")
    return op   
