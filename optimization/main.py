from optimization.gradient_descent import gd
from sympy import *

x = symbols('x')

if __name__ == "__main__":
    func = 2 * x + x ** 2 + 25
    _, final_value = gd(func, start=12, max_iter=1000)
    print(final_value)
