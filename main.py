from calculus_core import derivative


def main():
    print("~" * 60)
    print("КАЛЬКУЛЯТОР ПРОИЗВОДНЫХ")
    print("~" * 60)
    print("Поддерживаются стандартные математические функции: sin, cos, log, exp и др.")
    print("Для выхода введите 'exit'")
    print("~" * 60)

    while True:
        try:
            expression = input("\nВведите математическое выражение: ").strip()

            if expression.lower() == 'exit':
                break

            variable = input("Введите переменную дифференцирования (один символ): ").strip()

            if variable.lower() == 'exit':
                break

            print("\n" + "=" * 60)
            print(f"Выражение: {expression}")
            print(f"Переменная: {variable}")
            print("=" * 60)

            result = derivative(expression, variable)

            print(f"Результат: d/d{variable}({expression}) = {result}")

            print("=" * 60)

        except Exception as e:
            print(f"Неожиданная ошибка: {str(e)}")

if __name__ == "__main__":
    main()