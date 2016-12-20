# -*- coding: utf-8 -*-
import sys
import drawLine
import drawRectangle
import createCanvas
import bucketFill


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

def validateInput(input_var, firstCommand=False):
    
    input_var = input_var.strip()    
    flag = True
    if (input_var == 'Q'):
        sys.exit('Program Exiting')
    elif(input_var == ' ' or input_var == '' ):
        flag = False
        print('Please enter value instead of blank')        
    else:
        split_input = str.split(input_var , ' ')
        if(firstCommand):
            if (split_input[0] != 'C' or len(split_input) != 3):
                flag = False
                print('Format error. Input should be of type \'C w h\'')
        else: 
            if (split_input[0] != 'C' and split_input[0] != 'B' and split_input[0] != 'L' and split_input[0] != 'R' ):
                flag = False
                print('Invalid user input error')
            elif (split_input[0] == 'C' and len(split_input)!=3):
                flag = False
                print('Format error. Input should be of type \'C w h\' to create a canvas')
            elif (split_input[0] == 'L' and len(split_input)!=5):
                flag = False
                print('Format error. Input should be of type \'L x1 y1 x2 y2\' to draw a line')
            elif (split_input[0] == 'R' and len(split_input)!=5):
                flag = False
                print('Format error. Input should be of type \'R x1 y1 x2 y2\' to draw a rectangle')
            elif (split_input[0] == 'B' and len(split_input)!=4):
                flag = False
                print('Format error. Input should be of type \'B x y c\' for bucket fill')
    return(flag)    
    
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
        print("Here")
        op = bucketFill.fillBucket(inputVal , canvas)
    return op   
