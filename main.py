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

def main():
    print("~" * 60)
    print("КАЛЬКУЛЯТОР ДЛЯ МАТЕМАТИЧЕСКОГО АНАЛИЗА")
    print("~" * 60)
    print("Поддерживаются стандартные математические функции: sin, cos, log, exp и др.")
    print("Для выхода введите 'exit'")
    print("~" * 60)

    while True:
        try:
            print("Введите номер операции из данного списка: \n1. производная, \n2. производная порядка n, \n3. частная производная, \n4. вычисление неопределенного интеграла, \n5. вычисление определенного интеграла")
            operation = input()
            if operation.lower() == "exit":
                break
            number = 0
            if operation.isdigit():
                number = int(operation)
            if number == 1:
                if deriv_output(): break
            elif number == 2:
                print("Введите порядок дифференцирования:")
                n = input().lower()
                if not n.isdigit():
                    if n == "exit": break
                    print("Порядок дифференцирования должен быть целым числом!")
                elif deriv_output(int(n)):
                    break
            elif number == 3:
                if par_deriv_output(): break
            else:
                print("Введите целое число из списка!")

        except Exception as e:
            print(f"Неожиданная ошибка: {str(e)}")

if __name__ == "__main__":
    main()