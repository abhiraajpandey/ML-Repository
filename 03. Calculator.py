# Write a Python Program to make a simple calculator that can
# add, subtract, multiply and divide.

def get_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter valid numerical value.")
            return get_number(prompt)

        
def again():
    option=str(input("Press '0' to Exit, or Press '1' to start again:"))
    if option in ("0","exit","Exit"):
        return False
    elif option=="1":
        return True
    else:
        print("Enter valid option!")
        return again()
                
    
def addition():
    x=0.0
    n=round(get_number("Enter how many numbers to add:"))
    if n>0:
        print("Enter the numbers:")
        for i in range(0,n):
            x=x+get_number("")
        print(f"The sum of entered numbers is {x:.2f}")
    else:
        print("Please enter a positive number!")
        addition()
    
def substraction():
    x=get_number("Enter first number:")
    y=get_number("Enter second number:")
    z=x-y
    print(f"Difference between the numbers is: {z:.2f}")
    

def multiplication():
    x=1.0
    n=round(get_number("Enter how many numbers to be multiplied:"))
    if n>0:
        print("Enter the numbers:")
        for i in range(0,n):
            x=x*get_number("")
        print(f"The product of entered numbers is {x:.2f}")
    else:
        print("Please enter a positive number!")
        multiplication()
    
    
def division():
    x=get_number("Enter dividend number:")
    y=get_number("Enter divisor number:")
    if y != 0:        
        z=float(x/y)
        print(f"The value of division is:{z:.2f}")
    else:
        print("Error! Division by Zero. Try Again.")
        division()
    
        
def calculator():
    print("Select the operation you want to perform: \
    \n1 = Addition \
    \n2 = Substraction \
    \n3 = Multiplication \
    \n4 = Division \
    \n5 = Exit")
    option=str(input("Enter Choice:"))
    
    if option in ("5","exit","Exit"):
        exit
    elif option!=("5","exit","Exit"):
        if option in ('1', '2', '3', '4'):
            if option=="1":
                addition()
            elif option=="2":
                substraction()
            elif option=="3":
                multiplication()
            elif option=="4":
                division()
    
            if again():
                calculator()
        else:
            print("Enter valid option!")
            return calculator()
    
    
print("Welcome to Basic Calculator")
calculator()

