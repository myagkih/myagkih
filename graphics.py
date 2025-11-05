import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def plot_function(expression: str, variable: str, x_min: float, x_max: float) -> str:
    """
    Plot the graph of a mathematical function.

    Parameters:
        expression: mathematical expression as a string
        variable: variable for the x-axis
        x_min: minimum x value
        x_max: maximum x value

    Returns:
        Success message or error message
    """
    try:
        if len(variable) != 1 or not variable.isalpha():
            return "Error: Variable must be a single character"

        if not expression or not expression.strip():
            return "Error: Expression cannot be empty"

        if x_min >= x_max:
            return "Error: x_min must be less than x_max"

        f = sp.lambdify(sp.Symbol(variable), sp.sympify(expression), 'numpy')

        x_vals = np.linspace(x_min, x_max, 1000)

        y_vals = f(x_vals)

        plt.figure(figsize=(14, 8))
        plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'${sp.latex(sp.sympify(expression))}$')

        plt.xlabel(f'${variable}$', fontsize=12)
        plt.ylabel(f'$f({variable})$', fontsize=12)
        plt.legend(fontsize=12)

        plt.tight_layout()
        plt.show()

        return "Graph plotted successfully"

    except sp.SympifyError:
        return f"Error: Invalid expression '{expression}'"
    except Exception as e:
        return f"Error while plotting graph: {str(e)}"


if __name__ == "__main__":
    test_cases = [
        ("x**2", "x", -5, 5),
        ("sin(x)", "x", -2 * np.pi, 2 * np.pi),
        ("exp(-x**2)", "x", -3, 3),
    ]

    print("GRAPH PLOTTING TESTS")
    print("=" * 50)

    for expr, var, xmin, xmax in test_cases:
        print(f"Plotting graph: {expr} on [{xmin}, {xmax}]")
        result = plot_function(expr, var, xmin, xmax)
        print(f"Result: {result}")
        print("-" * 50)