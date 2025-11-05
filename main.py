from outputs import *

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
            elif number == 4:
                if indf_integral_output(): break
            else:
                print("Введите целое число из списка!")

        except Exception as e:
            print(f"Неожиданная ошибка: {str(e)}")

if __name__ == "__main__":
    main()