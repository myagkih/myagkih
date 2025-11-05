import sympy as sp


def derivative(expression: str, variable: str, n: int = 1) -> str:
    """
    Calculate the derivative of a mathematical expression with respect to a given variable.

    Parameters:
        expression: mathematical expression as a string
        variable: variable of differentiation
        n: order of derivative (default=1 for first derivative)

    Returns:
        String representation of the derivative or error message
    """
    try:
        if len(variable) != 1 or not variable.isalpha():
            return "Error: Variable must be a single character"

        if not expression or not expression.strip():
            return "Error: Expression cannot be empty"

        if n <= 0:
            return "Error: Order must be greater than 0"

        sym_var = sp.Symbol(variable)

        parsed_expr = sp.sympify(expression)

        simplified_result = sp.simplify(sp.diff(parsed_expr, sym_var, n))

        return str(simplified_result)

    except sp.SympifyError:
        return f"Error: Invalid expression {expression}"
    except Exception as e:
        return f"Error while calculating derivative: {str(e)}"


def partial_derivative(expression: str, variables: str) -> str:
    """
    Calculate partial derivatives for functions of multiple variables.

    Parameters:
        expression: mathematical expression as a string
        variables: string of variables for differentiation

    Returns:
        String representation of partial derivatives or error message
    """
    try:
        if not expression or not expression.strip():
            return "Error: Expression cannot be empty"

        if not variables or not variables.strip():
            return "Error: No differentiation variables specified"

        result = sp.sympify(expression)

        for var in variables:
            result = sp.diff(result, sp.Symbol(var))

        simplified_result = sp.simplify(result)
        return str(simplified_result)

    except sp.SympifyError:
        return f"Error: Invalid expression '{expression}'"
    except Exception as e:
        return f"Error while calculating partial derivative: {str(e)}"


if __name__ == "__main__":
    print("=" * 50)
    print("DERIVATIVE TESTS")
    print("=" * 50)

    ordinary_tests = [
        ("x**3", "x", 1),
        ("sin(x)", "x", 1),
    ]

    for expr, var, order in ordinary_tests:
        result = derivative(expr, var, order)
        print(f"d/d{var}({expr}) = {result}")

    print("\n" + "=" * 50)
    print("PARTIAL DERIVATIVE TESTS")
    print("=" * 50)

    partial_tests = [
        ("x**2 + y**2", "x", "2*x"),
        ("x**2 * y**3", "xy", "6*x*y**2"),
        ("sin(x)*cos(y)", "x", "cos(x)*cos(y)")
    ]

    for expr, vars, expected in partial_tests:
        result = partial_derivative(expr, vars)
        print(f"∂^{len(vars)}/(∂{vars})({expr}) = {result}")

    print("\n" + "=" * 50)
    print("ERROR TEST")
    print("=" * 50)
    print(partial_derivative("", "x"))

    print("=" * 50)