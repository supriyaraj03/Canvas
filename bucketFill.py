# -*- coding: utf-8 -*-
import wrapper
from numpy import array
import sys

################################################################################
# Fill the bucket on the canvas using the provided coordinates (x, y, c)
################################################################################

def fillBucket(inputVal, canvas):
    split_input = str.split(inputVal , ' ')
    canvas_width = len(canvas[1])-2
    canvas_height = len(canvas)-2
    
    try:
        x = int(split_input[1])
        y = int(split_input[2])
    except ValueError:
        sys.exit('Coordinates should be positive integers')
        
    if((x <= 0) or (y<= 0)):
        sys.exit('Coordinates should be positive integers')
    if((x > canvas_width) or (y > canvas_height)):
        sys.exit('You can draw only within the canvas')
    
    fill_value = split_input[3]
    
    canvas = array(canvas)
    xsize, ysize = canvas.shape
    orig_value = canvas[x , y]
    
    stack = set(((x , y),))
    if fill_value == orig_value:
        raise ValueError("Trying to fill region with same value")
                     
    while stack:
        x, y = stack.pop()
        print(x,y)
        if canvas[x, y] == orig_value:
            canvas[x, y] = fill_value
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))

    wrapper.printFunction(canvas , (len(canvas)-2))

    return (canvas)