import sympy as sp


def indefinite_integral(expression: str, variable: str) -> str:
    """
    Calculate the indefinite integral of a mathematical expression with respect to a given variable.

    Parameters:
        expression: mathematical expression as a string
        variable: variable of integration

    Returns:
        String representation of the indefinite integral or error message
    """
    try:
        if len(variable) != 1:
            return "Ошибка: Переменная должна быть одним символом"

        if not expression or not expression.strip():
            return "Ошибка: Выражение не может быть пустым"

        integral_result = sp.integrate(sp.sympify(expression), sp.Symbol(variable))

        return str(sp.simplify(integral_result))

    except sp.SympifyError:
        return f"Ошибка: Некорректное выражение '{expression}'"
    except Exception as e:
        return f"Ошибка при вычислении интеграла: {str(e)}"


def definite_integral(expression: str, variable: str, lower_limit: str, upper_limit: str) -> str:
    """
    Calculate the definite integral of a mathematical expression with respect to a given variable.

    Parameters:
        expression: mathematical expression as a string
        variable: variable of integration
        lower_limit: lower limit of integration
        upper_limit: upper limit of integration

    Returns:
        String representation of the definite integral result or error message
    """
    try:
        if len(variable) != 1:
            return "Ошибка: Переменная должна быть одним символом"

        if not expression or not expression.strip():
            return "Ошибка: Выражение не может быть пустым"

        sym_var = sp.Symbol(variable)
        parsed_expr = sp.sympify(expression)

        integral_result = sp.integrate(parsed_expr, (sym_var, sp.sympify(lower_limit), sp.sympify(upper_limit)))

        return str(sp.simplify(integral_result))

    except sp.SympifyError:
        return f"Ошибка: Некорректное выражение или пределы интегрирования"
    except Exception as e:
        return f"Ошибка при вычислении интеграла: {str(e)}"


if __name__ == "__main__":
    test_cases = [
        ("x**2", "x"),
        ("cos(x)", "x"),
        ("1/x", "x"),
        ("exp(x)", "x"),
    ]

    print("ТЕСТЫ НЕОПРЕДЕЛЕННЫХ ИНТЕГРАЛОВ")
    print("=" * 50)

    for expr, var in test_cases:
        result = indefinite_integral(expr, var)
        print(f"∫({expr}) d{var} = {result}")

    test_cases = [
        ("x**2", "x", "0", "1"),
        ("cos(x)", "x", "0", "pi/2"),
        ("1", "x", "a", "b"),
        ("2*x + 3", "x", "0", "2"),
        ("exp(x)", "x", "0", "1"),
    ]

    print("ТЕСТЫ ОПРЕДЕЛЕННЫХ ИНТЕГРАЛОВ")
    print("=" * 50)

    for expr, var, lower, upper in test_cases:
        result = definite_integral(expr, var, lower, upper)
        print(f"∫[{lower}→{upper}]({expr}) d{var} = {result}")