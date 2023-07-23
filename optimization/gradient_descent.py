import numpy as np
from sympy import *


def gd(f, start, max_iter, learning_rate=0.01, tol=0.01):
    steps = [start]
    y = start
    x = symbols('x')
    for _ in range(max_iter):
        step_size = learning_rate * diff(f, x).subs(x, y).evalf()
        if np.abs(step_size) < tol:
            break
        y = y - step_size
        steps.append(y)

    final_value = steps[len(steps)-1]

    return steps, final_value
