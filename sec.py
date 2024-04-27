
import sympy as sp
import sympy.parsing.sympy_parser as spp
import re


def is_valid_expression(expression):
    try:
        spp.parse_expr(expression, evaluate=False)
        return True
    except (spp.SympyParserError, sp.SympifyError):
        return False


def bisection_method(func, a, b, N,tol=1e-6):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
    


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

    n=int(input("N:"))
    root = bisection_method(f, a, b , n)

    
    print(f"The root is approximately: {root:.{precision}f}")
    
