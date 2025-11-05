"""
Модуль для символьных математических вычислений с использованием библиотеки SymPy.
Предоставляет функции для вычисления производных математических выражений.
"""

import sympy as sp


def derivative(expression: str, variable: str) -> str:
    """
    Calculate the derivative of a mathematical expression with respect to a given variable.

    Parameters:
        expression: mathematical expression as a string
        variable: variable of differentiation

    Returns:
        String representation of the derivative or error message
    """
    try:
        if len(variable) != 1 or not variable.isalpha():
            return "Ошибка: Переменная должна быть одним символом"

        if not expression or not expression.strip():
            return "Ошибка: Выражение не может быть пустым"

        sym_var = sp.Symbol(variable)

        parsed_expr = sp.sympify(expression)

        simplified_result = sp.simplify(sp.diff(parsed_expr, sym_var))

        return str(simplified_result)

    except sp.SympifyError:
        return f"Ошибка: Некорректное выражение {expression}"
    except Exception as e:
        return f"Ошибка при вычислении производной: {str(e)}"


if __name__ == "__main__":
    test_cases = [
        ("x**2", "x"),
        ("sin(x)", "x"),
        ("invalid expression", "x"),
    ]

    for expr, var in test_cases:
        result = derivative(expr, var)
        print(f"Производная {expr} по {var}: {result}")