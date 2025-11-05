from calculus_core import *
from integrals import *
from graphics import *

def graph_view():
    expression = input("\nEnter mathematical expression: ").strip()

    if expression.lower() == 'exit':
        return True

    variable = input("Enter variable for X axis: ").strip()

    if variable.lower() == 'exit':
        return True

    try:
        x_min, x_max = 0, 0
        input_ = input("Enter minimum X value: ").strip()
        if input_ == "exit":
            return True
        else:
            x_min = float(input_)

        input_ = input("Enter maximum X value: ").strip()
        if input_ == "exit":
            return True
        else:
            x_max = float(input_)

        print(plot_function(expression, variable, x_min, x_max))
    except ValueError:
        print("Error: x_min and x_max must be numbers")

def integral_output():
    expression = input("\nEnter mathematical expression: ").strip()

    if expression.lower() == 'exit':
        return True

    variable = input("Enter integration variable: ").strip()

    if variable.lower() == 'exit':
        return True

    lower = input("Enter lower limit: ").strip()

    if lower.lower() == 'exit':
        return True

    upper = input("Enter upper limit: ").strip()

    if upper.lower() == 'exit':
        return True

    print("=" * 60)
    result = definite_integral(expression, variable, lower, upper)
    print(f"∫[{lower}→{upper}]({expression}) d{variable} = {result}")
    print("=" * 60)

    return False

def indf_integral_output():
    expression = input("\nEnter mathematical expression: ").strip()

    if expression.lower() == 'exit':
        return True

    variable = input("Enter integration variable: ").strip()

    if variable.lower() == 'exit':
        return True

    print("=" * 60)
    result = indefinite_integral(expression, variable)
    print(f"∫({expression}) d{variable} = {result}")
    print("=" * 60)
    return False

def par_deriv_output():
    expression = input("\nEnter mathematical expression: ").strip()

    if expression.lower() == 'exit':
        return True

    variables = input("Enter differentiation variables (e.g., 'xy'): ").strip()

    if variables.lower() == 'exit':
        return True

    print("\n" + "=" * 60)
    result = partial_derivative(expression, variables)
    print(f"∂^{len(variables)}/({''.join(f'∂{v}' for v in variables)})({expression}) = {result}")
    print("=" * 60)

    return False

def deriv_output(n: int = 1):
    expression = input("\nEnter mathematical expression: ").strip()

    if expression.lower() == 'exit':
        return True

    variable = input("Enter differentiation variable (single character): ").strip()

    if variable.lower() == 'exit':
        return True

    print("\n" + "=" * 60)
    print(f"Expression: {expression}")
    print(f"Variable: {variable}")
    print("=" * 60)

    result = derivative(expression, variable, n)
    if n > 1:
        print(f"Result: derivative({expression} of order {n}) = {result}")
    else:
        print(f"Result: d/d{variable}({expression}) = {result}")

    print("=" * 60)
    return False