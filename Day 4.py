#Creating a calculator
def add(x,y):
    '''Add two Numbers and Return result'''
    return x+y
def subtract(x,y):
    '''Subtract two Numbers '''
    return x-y
def multiply(x,y):
    '''Multipy two Numbers '''
    return x*y
def divide(x,y):
    '''Divide two Numbers '''
    if y==0:
        return "Error: You can not divide by zero"
    return x/y
def power(x,y):
    '''Raise x to power y'''
    return x**y
#User Input and Choice
x=float(input("Enter The value of x:"))
y=float(input("Enter The value of y:"))
o=input("Enter the Operation:")
if o=="Addtion":
    result=add(x,y)
elif o=="Subraction":
    result=subract(x,y)
elif o=="Multiplication":
    result=multiply(x,y)
elif o=="Division":
    result=divide(x,y)
elif o=="Power":
    result=power(x,y)
else:
    print("Invalid Choice")
print("Result:",result)












    
