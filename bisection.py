import sympy as sp
import sympy.parsing.sympy_parser as spp
import re

def is_valid_expression(expression):
    try:
        
        parsed_expr = spp.parse_expr(expression, evaluate=False)
        return True
    except (spp.SympyParserError, sp.SympifyError):
        return False


def bisection_method(func, a, b):
    prec = input("\nSpecify a precision ... \nExample:\n1.01 or 1.001 ...etc \n\nPlease provide an integer: ")
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while ((b-a) >= 0.01):
 
        
        c = (a+b)/2
  
        
        if (func(c) == 0.0):
            break
  
        
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ",f"%.{prec}f"%c)


expression = input("Enter the function expression in terms of x (e.g., x**3 - 2*x - 2): ")
if not is_valid_expression(expression):
    print("Invalid expression. Please enter a valid mathematical expression.")
else:
    x = sp.symbols('x')
    f = sp.lambdify(x, spp.parse_expr(expression, evaluate=False))

   
    while True:

        a = float(input("Enter the start of the interval (a): "))
        b = float(input("Enter the end of the interval (b): "))
        if f(a) * f(b) > 0:
            print("The function does not change signs over this interval. Please try again.")
        else:
            break



    if 'a' in locals() and 'b' in locals():
        root = bisection_method(f, a, b)
  