print("Select an operation: ")
print("1 - Add")
print("2 - Sub")
print("3 - Mul")
print("4 - Div")

Choose = int(input("Enter an operation: "))

if(Choose  in [1,2,3,4]):
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if(Choose == 1):
        ans = n1 + n2 
    elif(Choose == 2):
        ans = n1-n2 
    elif(Choose == 3):
        ans = n1 * n2 
    elif(Choose == 4):
        ans = n1//n2 

else:
    print("Invalid Choose operation")
print("The ans of the operation is {}".format(ans))        
