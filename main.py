import wrapper

######################################
# User input is accepted and processed
######################################       
def main():
    input_var = input("enter command: ")
    wrapper.validateInput(input_var , firstCommand=True)
    op = wrapper.performOperation(input_var)
    
    while True:
        input_var = input("enter command: ")
        wrapper.validateInput(input_var)
        op = wrapper.performOperation(input_var , op)
        
#Entry point     CCC
if __name__ == '__main__':
    main()
