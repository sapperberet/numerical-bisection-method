import sympy as sp
import sympy.parsing.sympy_parser as spp
import re


def is_valid_expression(expression):
    try:
        spp.parse_expr(expression, evaluate=False)
        return True
    except (spp.SympyParserError, sp.SympifyError):
        return False


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function does not change signs over the interval [a, b].")
    
    c = (a + b) / 2.0
    for i in range(max_iter):
        c = (a + b) / 2.0
        
        
        if abs(func(c)) < tol or (b - a) / 2.0 < tol:
            break
        
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    
    error = (b - a) / 2.0
    return c, error


expression = input("Enter the function expression in terms of x (ex: x**3 - 2*x - 2): ")


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
    
    
    # precision = int(input("Specify the number of decimal places for precision: "))
    precision = int(input("\nSpecify a precision ... \n\nExample:\n1.01 , 1.001 or 1.0001 ...etc \n\nPlease provide an integer: "))

    
    root, error = bisection_method(f, a, b)

    
    print(f"The root is approximately: {root:.{precision}f}")
    print(f"The estimated error in the root value is: ±{error:.{precision}f}")
