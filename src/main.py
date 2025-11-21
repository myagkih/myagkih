from modules.outputs import *

def main():
    print("~" * 60)
    print("CALCULUS CALCULATOR")
    print("~" * 60)
    print("Supported standard mathematical functions: sin, cos, log, exp, etc.")
    print("Enter 'exit' to quit")
    print("~" * 60)

    while True:
        try:
            print("Enter operation number from the list: \n1. derivative, \n2. nth order derivative, \n3. partial derivative, \
             \n4. indefinite integral, \n5. definite integral, \n6. function graph plotting")
            operation = input()
            if operation.lower() == "exit":
                break
            number = 0
            if operation.isdigit():
                number = int(operation)
            if number == 1:
                if deriv_output(): break
            elif number == 2:
                print("Enter differentiation order:")
                n = input().lower()
                if not n.isdigit():
                    if n == "exit": break
                    print("Differentiation order must be an integer!")
                elif deriv_output(int(n)):
                    break
            elif number == 3:
                if par_deriv_output(): break
            elif number == 4:
                if indf_integral_output(): break
            elif number == 5:
                if integral_output(): break
            elif number == 6:
                if graph_view(): break
            else:
                print("Enter an integer from the list!")

        except Exception as e:
            print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
