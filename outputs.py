from calculus_core import *

def par_deriv_output():
    expression = input("\nВведите математическое выражение: ").strip()

    if expression.lower() == 'exit':
        return True

    variables = input("Введите переменные дифференцирования (например, 'xy'): ").strip()

    if variables.lower() == 'exit':
        return True

    print("\n" + "=" * 60)
    result = partial_derivative(expression, variables)
    print(f"∂^{len(variables)}/({''.join(f'∂{v}' for v in variables)})({expression}) = {result}")
    print("=" * 60)

    return False


def deriv_output(n: int = 1):
    expression = input("\nВведите математическое выражение: ").strip()

    if expression.lower() == 'exit':
        return True

    variable = input("Введите переменную дифференцирования (один символ): ").strip()

    if variable.lower() == 'exit':
        return True

    print("\n" + "=" * 60)
    print(f"Выражение: {expression}")
    print(f"Переменная: {variable}")
    print("=" * 60)

    result = derivative(expression, variable, n)

    print(f"Результат: d/d{variable}({expression}) = {result}")

    print("=" * 60)
    return False