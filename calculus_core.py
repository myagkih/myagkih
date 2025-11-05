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
            return "Ошибка: Переменная должна быть одним символом"

        if not expression or not expression.strip():
            return "Ошибка: Выражение не может быть пустым"

        if n <= 0:
            return "Ошибка: порядок должен быть больше 0"

        sym_var = sp.Symbol(variable)

        parsed_expr = sp.sympify(expression)

        simplified_result = sp.simplify(sp.diff(parsed_expr, sym_var, n))

        return str(simplified_result)

    except sp.SympifyError:
        return f"Ошибка: Некорректное выражение {expression}"
    except Exception as e:
        return f"Ошибка при вычислении производной: {str(e)}"


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
            return "Ошибка: Выражение не может быть пустым"

        if not variables or not variables.strip():
            return "Ошибка: Не указаны переменные дифференцирования"

        parsed_expr = sp.sympify(expression)
        result = parsed_expr

        for var in variables:
            sym_var = sp.Symbol(var)
            result = sp.diff(result, sym_var)

        simplified_result = sp.simplify(result)
        return str(simplified_result)

    except sp.SympifyError:
        return f"Ошибка: Некорректное выражение '{expression}'"
    except Exception as e:
        return f"Ошибка при вычислении частной производной: {str(e)}"


if __name__ == "__main__":
    test_cases = [
        ("x**2", "x"),
        ("sin(x)", "x"),
        ("invalid expression", "x"),
    ]

    for expr, var in test_cases:
        result = derivative(expr, var)
        print(f"Производная {expr} по {var}: {result}")