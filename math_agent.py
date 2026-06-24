import math

class MathAgent:
    def __init__(self):
        self.name = "Hermione_Math_Agent"

    def calculate(self, operation, *args):
        """
        Processes mathematical operations based on user input.
        """
        operation = operation.lower().strip()

        try:
            # 1. Basic Arithmetic
            if operation == "add":
                return f"Result: {sum(args)}"
            
            elif operation == "subtract":
                if len(args) < 2: return "Error: Need at least two numbers to subtract."
                result = args[0]
                for num in args[1:]:
                    result -= num
                return f"Result: {result}"
            
            elif operation == "multiply":
                if not args: return "Result: 0"
                result = 1
                for num in args:
                    result *= num
                return f"Result: {result}"
            
            elif operation == "divide":
                if len(args) < 2: return "Error: Need at least two numbers to divide."
                result = args[0]
                for num in args[1:]:
                    if num == 0:
                        return "Error: Cannot divide by zero!"
                    result /= num
                return f"Result: {result}"

            # 2. Advanced Math
            elif operation == "power":
                if len(args) != 2: return "Error: Provide a base and an exponent (e.g., 2, 3)."
                return f"Result: {math.pow(args[0], args[1])}"
            
            elif operation == "sqrt" or operation == "square root":
                if len(args) != 1: return "Error: Provide exactly one number."
                if args[0] < 0: return "Error: Cannot find square root of a negative number."
                return f"Result: {math.sqrt(args[0])}"
            
            elif operation == "factorial":
                if len(args) != 1: return "Error: Provide exactly one integer."
                if args[0] < 0 or not float(args[0]).is_integer():
                    return "Error: Factorial requires a positive whole number."
                return f"Result: {math.factorial(int(args[0]))}"

            # 3. Geometry Tools
            elif operation == "circle area":
                if len(args) != 1: return "Error: Provide the radius of the circle."
                area = math.pi * math.pow(args[0], 2)
                return f"Result: The area of the circle is {round(area, 4)}"

            else:
                return f"Unknown operation. Available tools: add, subtract, multiply, divide, power, sqrt, factorial, circle area."

        except Exception as e:
            return f"An error occurred during calculation: {str(e)}"

# Interactive loop to run the Math Agent
if __name__ == "__main__":
    agent = MathAgent()
    print(f"=== {agent.name} is online ===")
    print("Type 'exit' to stop.")
    print("Commands format: operation, number1, number2... (Example: add, 5, 10)")
    print("-" * 40)

    while True:
        user_input = input("Enter command: ")
        if user_input.lower().strip() == "exit":
            print("Shutting down Math Agent. Goodbye!")
            break
        
        # Split the input by commas to separate operation and numbers
        parts = user_input.split(",")
        if not parts or parts[0] == "":
            continue
            
        op = parts[0]
        
        # Convert the remaining parts into numbers
        try:
            numbers = [float(p.strip()) for p in parts[1:] if p.strip() != ""]
            response = agent.calculate(op, *numbers)
            print(response)
            print("-" * 40)
        except ValueError:
            print("Error: Please provide valid numbers separated by commas.")
            print("-" * 40)