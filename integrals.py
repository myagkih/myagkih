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