# -*- coding: utf-8 -*-
import wrapper

######################################
# User input is accepted and processed
######################################       

def main():
    
    while True:
        input_var = input("enter command: ")
        flag = wrapper.validateInput(input_var , firstCommand=True)
        if not flag:
            continue
        else:
            op = wrapper.performOperation(input_var)
            break

    while True:
        input_var = input("enter command: ")
        flag = wrapper.validateInput(input_var)
        if not flag:
            continue
        else:
            op = wrapper.performOperation(input_var , op)
        
        
#Entry point     CCC
if __name__ == '__main__':
    main()