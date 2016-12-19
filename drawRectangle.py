# -*- coding: utf-8 -*-
import sys
import wrapper


################################################################################
# Draw a rectangle on the canvas using the provided coordinates (x1, y1, x2, y2)
################################################################################
def createRectangle(inputVal , canvas):
    
    split_input = str.split(inputVal , ' ')
    canvas_width = len(canvas[1])-2
    canvas_height = len(canvas)-2

    try:
        x1= int(split_input[1])
        y1= int(split_input[2])
        x2= int(split_input[3])
        y2= int(split_input[4])
    except ValueError:
        sys.exit('Coordinates should be positive integers')
        
    if((x1 <= 0) or (y1<= 0) or
        (x2 <= 0) or (y2<= 0)):
        sys.exit('Coordinates should be positive integers')
    if((x1 > canvas_width) or (x2 > canvas_width) or 
        (y1 > canvas_height) or (y2 > canvas_height)):
        sys.exit('You can draw only within the canvas')
        
    if(x2 >= x1):
        for i in range(x1 , (x2+1)):
            canvas[y1][i] = 'x'
            canvas[y2][i] = 'x'
    else:
        for i in range(x2 , (x1+1)):
            canvas[y1][i] = 'x'
            canvas[y2][i] = 'x'
    
    if(y2 >= y1):    
        for i in range(y1 , y2):
            canvas[i][x1] = 'x'
            canvas[i][x2] = 'x'
    else:
        for i in range(y2 , y1):
            canvas[i][x1] = 'x'
            canvas[i][x2] = 'x'
        
    wrapper.printFunction(canvas , canvas_height) 
    
    return(canvas)