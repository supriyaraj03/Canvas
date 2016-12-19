# Canvas with basic functionality
 
This program creates a canvas based on the user input and also wraps up with some basic functionalities that can be done in the canvas.
Basic functionalities are:
1 Draw Lines, 2 Draw Rectangle and 3 Bucket fill
 
## Getting Started
 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Run the code with the main class to get it start running.
 
### Prerequisites
 
```
Python version 3.5.2 has to be installed (should work on 3.x, but not tested)
```
 
## Code Structure
 
A separate method has been implemented for each functionality:
1) Create canvas (createCanvas.py)
2) Draw straight line on the canvas (drawLine.py)
3) Draw rectangle on the canvas(drawRectangle.py)
4) Bucket fill using the required color (bucketFill.py)

A method has been defined in the wrapper.py to print the matrix in the canvas format.

A method has been defined in the wrapper.py to validate the input from the user

User can perform the above mentioned actions, as well as quit the program if he wishes to terminate.

## For Users

To create a canvas, user input must be of type: C x y
To draw a line, user input must be of type: C x1 y1 x2 y2
To draw a rectangle, user input must be of type: R x1 y1 x2 y2
For bucket fill, user input must be of type: B x y <color>
To quit, user input must be of type: Q

## Design Strategies

Application is developed keeping in mind:
1) Readability (also well commented and proper naming conventions are used)
2) Computational complexity (O(n)). The tricky part arises in the bucket fill module, where I used a stack to compute in the optimal way.
3) Modularity (split the code into multiple files as per the functionality)


## How to run?

```
python main.py
```