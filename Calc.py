class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a
        
    def multiply(self, a, b):
        if a < 0 or b < 0:
            raise ValueError
        return a * b
        
    
class Calc:
    def __init__(self) -> None:
        self.calc = Calculator()

    def input(self):
        print('Enter your choice. \n 1. Add \n 2. Subtract \n 3. Multiplication')

        choice = int(input())

        if choice not in [1,2,3,4]:
            print('Invalid choice. Please choose between 1 and 4')


        op1 = int(input("Enter the first number "))
        op2 = int(input("Enter the second number "))

        if choice == 1:
            result = self.calc.add(op1, op2)
            print(f"Result: {result}")
        elif choice == 2:
            result = self.calc.subtract(op1, op2)
            print(f"Result: {result}")
        elif choice == 3:
            result = self.calc.multiply(op1, op2)
            print(f"Result:{result}")

    def run(self):
        self.input()



if __name__ == '__main__':
    app = Calc()
    app.run()
