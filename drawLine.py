# -*- coding: utf-8 -*-
import sys
import wrapper

###########################################################################
# Draw a line on the canvas using the provided coordinates (x1, y1, x2, y2)
###########################################################################
def createLine(inputVal , canvas):
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
    if(not ((x1==x2) or (y1==y2) )):
        sys.exit('Only straight lines are allowed')
    if((x1 > canvas_width) or (x2 > canvas_width) or 
        (y1 > canvas_height) or (y2 > canvas_height)):
        sys.exit('You can draw only within the canvas')

    if(x1 == x2):
        if(y2 >= y1):
            for i in range(y1,(y2+1)):
                canvas[i][x1] = 'x'                
        else:
            for i in range(y2,(y1+1)):
                canvas[i][x1] = 'x'                
    elif(y1 == y2):
        if(x2 >= x1):
            for i in range(x1,(x2+1)):
                canvas[y1][i] = 'x'                
        else:
            for i in range(x2,(x1+1)):
                canvas[y1][i] = 'x'                
            
    wrapper.printFunction(canvas , canvas_height)
    
    return(canvas)