from calculator import Calculator, CalculatorError

def menu():
    calc = Calculator()
    while True:
        print("\nScientific Calculator")
        print("1) sqrt(x)")
        print("2) factorial(n)")
        print("3) ln(x)")
        print("4) x^b")
        print("5) exit")
        choice = input("Choose [1-5]: ").strip()
        try:
            if choice == '1':
                x = float(input("x = "))
                print("=>", calc.sqrt(x))
            elif choice == '2':
                n = float(input("n = "))
                print("=>", calc.factorial(n))
            elif choice == '3':
                x = float(input("x = "))
                print("=>", calc.ln(x))
            elif choice == '4':
                x = float(input("x = "))
                b = float(input("b = "))
                print("=>", calc.power(x, b))
            elif choice == '5':
                break
            else:
                print("Invalid choice")
        except CalculatorError as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()
